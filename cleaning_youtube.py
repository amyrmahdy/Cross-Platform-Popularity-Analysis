from general import convert_metric

 
def drop_useless_cols_youtube(df):
    return df.drop(["Country","Category_3","Category_2","S.no"], axis = 1)

def converting_youtube(df):
    youtube_convert_list = ["subscribers", "views_avg","likes_avg", "comments_avg" ]

    for item_youtube in youtube_convert_list:
        df[item_youtube] = df[item_youtube].apply(lambda x: convert_metric(x)).astype(int)
    return df

def rename_youtube(df):
    df.rename( columns={
        "Youtuber": "youtuber",
        "Name" : "name",
        "Subscribers" : "subscribers",
        "Avg. views" : "views_avg",
        "Avg. likes" : "likes_avg",
        "Avg Comments" : "comments_avg"
    }, inplace = True)
    return df

def sort_values_youtube(df):
    return df.sort_values(by = "subscribers", ascending = False).reset_index(drop = True)