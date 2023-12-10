import os, glob

# requirementsファイルのリスト
PROJECTS_PATH = './analysis_projects'
projects = glob.glob('{}/*'.format(PROJECTS_PATH))
files = list(map(lambda x: x + '/requirements.txt', projects))
files.append('./requirements_all.txt')

# 依存関係を格納するセット
dependencies = set()

try:
    # 各ファイルから依存関係を読み込み
    for file in files:
        with open(file, 'r') as f:
            dependencies.update(f.readlines())
    
    # 重複を取り除き、新しいrequirementsファイルを作成
    with open('./requirements_all.txt', 'w') as f:
        for dependency in sorted(dependencies):
            f.write(dependency)
except Exception as e:
    print('EEROR: {}'.format(e))