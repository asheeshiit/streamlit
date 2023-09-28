import streamlit as st
from datetime import datetime
from google.cloud import bigquery
import pandas as pd
import sys



def get_channel_diff_conf_df(df2):
    col_list = list(df2.columns)
    if len(df2) > 1:
        diff_col_list = []
        for c in col_list:
            if len(pd.unique(df2[c])) > 1:
                diff_col_list.append(c)
        df2 = df2[diff_col_list]
    df2 = df2.drop(['ssai_configuration_ad_decision_configuration_0_ad_tags_0_url'], axis=1)

    return df2.transpose()


def compare_supply_tag_macros(client,list_of_supply_tag_ids):
    qr = '''
    WITH
      t1 AS (
      SELECT
        Supply_Tag_ID,
        SUM(Total_Requests) AS Total_Requests,
        SUM(Total_Impressions) AS Total_Impressions,
        SUM(Total_Impressions)/SUM(Total_Requests) AS pod_fill_rate
      FROM
        ads-development-382806.asheesh.supply_tag_18Jun_17jul23
      WHERE
        Total_Requests>0
        AND Supply_Tag_ID IN {}
      GROUP BY    
        Supply_Tag_ID),
      t2 AS (
      SELECT
        t1.*,
        a.Channel_ID
      FROM
        ads-development-382806.asheesh.thunderstorm_channels a
      JOIN
        t1
      ON
        t1.Supply_Tag_ID=a.Entity_ID )
    SELECT
      t2.Supply_Tag_ID,
      t2.Total_Requests,
      t2.Total_Impressions,
      t2.pod_fill_rate,
      b.*
    FROM
      ads-development-382806.asheesh.ts_channel_parsed_configs b
    JOIN
      t2
    ON
      t2.Channel_ID=b.Channel_ID
    '''.format(tuple(list_of_supply_tag_ids))

    df = client.query(qr).to_dataframe()
    return get_channel_diff_conf_df(df)

if __name__ == "__main__":
    client = bigquery.Client()
    supply_tag_list = client.query("select distinct(Entity_ID) as supply_tags from ads-development-382806.asheesh.thunderstorm_channels").to_dataframe()["supply_tags"].values.tolist()
    options = st.multiselect('Please select the supply tags',supply_tag_list)
    if st.button('Macro Comparision data against the selected supply atsg'):
        # st.write('You selected:', options)
        st.write(compare_supply_tag_macros(client,options))
