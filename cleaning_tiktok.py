from general import convert_metric

 
def check_name_problem_tiktok(df):
    if "Avg. views\r\n" not in df.columns:
        df.rename(columns = {"Avg. views\n": "Avg. views\r\n"})
    return df

def drop_useless_cols_tiktok(df):
    return df.drop(["S.no"], axis = 1)

def converting_tiktok(df):
    df["Views avg."] = df["Views avg."].apply(lambda x: convert_metric(x)).astype(int)
    df["Likes avg."] = df["Likes avg."].apply(lambda x: convert_metric(x)).astype(int)
    df["Comments avg."] = df["Comments avg."].apply(lambda x: convert_metric(x)).astype(int)
    df["Shares avg."] = df["Shares avg."].apply(lambda x: convert_metric(x)).astype(int)
    return df

def rename_tiktok(df):
    df.rename( columns={
        "Tiktoker name": "tiktoker",
        "Tiktok name" : "name",
        "Subscribers" : "subscribers",
        "Views avg." : "views_avg",
        "Likes avg." : "likes_avg",
        "Comments avg." : "comments_avg",
        "Shares avg.": "shares_avg"
    }, inplace = True)
    return df

def sort_values_tiktok(df):
    return df.sort_values(by = "subscribers", ascending = False).reset_index(drop = True)