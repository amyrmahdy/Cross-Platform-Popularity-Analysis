from general import convert_metric



def drop_useless_cols_instagram(df):
    return df.drop(["S.no","Audience country","Authentic engagement","Category_1","Category_2"], axis = 1)

def converting_instagram(df):
    instagram_convert_list = ["subscribers", "engagement_avg"]

    for item_instagram in instagram_convert_list:
        df[item_instagram] = df[item_instagram].apply(lambda x: convert_metric(x)).astype(int)
    return df

def rename_instagram(df):
    df.rename( columns={
    "Instagram name": "id",
    "Name" : "name",
    "Subscribers" : "subscribers",
     "Engagement average" : "engagement_avg"
    }, inplace = True)
    return df

def sort_values_instagram(df):
    return df.sort_values(by = "subscribers", ascending = False).reset_index(drop = True)