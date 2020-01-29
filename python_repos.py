import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#  执行api调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#  将api响应储存在一个变量中
response_dict = r.json()

#  处理结果 打印字典的键
print('总数', response_dict['total_count'])

#  探索仓库有关信息
repo_dicts = response_dict['items']
print('仓库数量', len(repo_dicts))

#  研究第一个仓库
repo_dict = repo_dicts[0]

names, plot_dicts = [], []
print("\n最受欢迎的python仓库:")
for repo_dict in repo_dicts:
    # print('\n项目名称:', repo_dict['name'])
    # print('登录名:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('地址:', repo_dict['html_url'])
    # print('创建时间:', repo_dict['created_at'])
    # print('更新时间:', repo_dict['updated_at'])
    # print('仓库描述:', repo_dict['description'])
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] if repo_dict['description'] else ' ',
        #  添加可单击的链接
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

#  可视化
my_style = LS('#333366', base_stayle=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'github-python仓库star统计'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

