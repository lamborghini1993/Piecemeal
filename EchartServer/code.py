import web
from web import form
urls = (
    '/(.*)', 'index',
)

# dInfo2 = {
#     "legend_data": ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎'],
#     "xAxis_data": ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
#     "series_data": [
#         {
#             "name": '邮件营销',
#             "type": 'line',
#             "data": [120, 132, 101, 134, 90, 230, 210]
#         },
#         {
#             "name": '联盟广告',
#             "type": 'line',
#             "data": [220, 182, 191, 234, 290, 330, 310]
#         },
#         {
#             "name": '视频广告',
#             "type": 'line',
#             "data": [150, 232, 201, 154, 190, 330, 410]
#         },
#         {
#             "name": '直接访问',
#             "type": 'line',
#             "data": [320, 332, 301, 334, 390, 330, 320]
#         },
#         {
#             "name": '搜索引擎',
#             "type": 'line',
#             "data": [820, 932, 901, 934, 1290, 1330, 10]
#         }
#     ]
# }

dInfo = {
    "legend_data": ['one', 'two', 'three', 'four', 'five'],
    "xAxis_data": ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    "series_data": [
        {
            "name": 'one',
            "type": 'line',
            "data": [120, 132, 101, 134, 90, 230, 210]
        },
        {
            "name": 'two',
            "type": 'line',
            "data": [220, 182, 191, 234, 290, 330, 310]
        },
        {
            "name": 'three',
            "type": 'line',
            "data": [150, 232, 201, 154, 190, 330, 410]
        },
        {
            "name": 'four',
            "type": 'line',
            "data": [320, 332, 301, 334, 390, 330, 320]
        },
        {
            "name": 'five',
            "type": 'line',
            "data": [820, 932, 901, 934, 1290, 1330, 10]
        }
    ]
}

class index:
    def GET(self, name):
        print(name)
        return dInfo


if __name__ == "__main__":
    app = web.application(urls, globals(), True)
    app.run()
