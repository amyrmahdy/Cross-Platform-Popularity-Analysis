from general import convert_metric

 
def check_name_problem_youtube(df):
    if "Avg. views\r\n" not in df.columns:
        df.rename(columns = {"Avg. views\n": "Avg. views\r\n"})
    return df

def drop_useless_cols_youtube(df):
    return df.drop(["Country","Category_3","Category_2","S.no"], axis = 1)

def converting_youtube(df):
    df[" Subscribers"] = df[" Subscribers"].apply(lambda x: convert_metric(x)).astype(int)
    df["Avg. views\r\n"] = df["Avg. views\r\n"].apply(lambda x: convert_metric(x)).astype(int)
    df["Avg. likes"] = df["Avg. likes"].apply(lambda x: convert_metric(x)).astype(int)
    df["Avg Comments"] = df["Avg Comments"].apply(lambda x: convert_metric(x)).astype(int)
    return df

def rename_youtube(df):
    df.rename( columns={
        "Youtuber": "youtuber",
        "Name" : "name",
        " Subscribers" : "subscribers",
        "Avg. views\r\n" : "views_avg",
        "Avg. likes" : "likes_avg",
        "Avg Comments" : "comments_avg"
    }, inplace = True)
    return df

def sort_values_youtube(df):
    return df.sort_values(by = "subscribers", ascending = False).reset_index(drop = True)