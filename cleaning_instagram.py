from general import convert_metric

 
def check_name_problem_instagram(df):
    if "Engagement average\r\n" not in df.columns:
        df.rename(columns = {"Engagement average\n": "Engagement average\r\n"})
    return df

def drop_useless_cols_instagram(df):
    return df.drop(["S.no","Audience country","Authentic engagement\n","Category_1","Category_2"], axis = 1)

def converting_instagram(df):
    df["Engagement average\r\n"] = df["Engagement average\r\n"].apply(lambda x: convert_metric(x)).astype(int)
    df["Subscribers"] = df["Subscribers"].apply(lambda x: convert_metric(x)).astype(int)
    return df

def rename_instagram(df):
    df.rename( columns={
    "Instagram name": "id",
    "Name" : "name",
    "Subscribers" : "subscribers",
    "Engagement average\r\n" : "engagement_avg"
    }, inplace = True)
    return df

def sort_values_instagram(df):
    return df.sort_values(by = "subscribers", ascending = False).reset_index(drop = True)