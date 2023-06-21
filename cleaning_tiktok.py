from general import convert_metric


def drop_useless_cols_tiktok(df):
    return df.drop(["S.no"], axis = 1)

def converting_tiktok(df):
    tiktok_convert_list = ["subscribers", "views_avg","likes_avg", "comments_avg", "shares_avg" ]

    for item_tiktok in tiktok_convert_list:
        df[item_tiktok] = df[item_tiktok].apply(lambda x: convert_metric(x)).astype(int)
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