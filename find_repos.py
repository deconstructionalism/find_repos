import crayons
import os
from subprocess import Popen
from git import Repo


dir_paths = [
    '~/Projects',
    '~/General Assembly'
]

ghub_origin_match_strings = [
    'git@github.com:deconstructionalism/',
    'git@github.com:ArjunRayGA/',
    'git@github.com:ga-students/DS-BOS-19',
    'git@github.com:ga-students/DS-BOS-Klaviyo',
    'git@git.generalassemb.ly:ga-ds-bos/',
    'https://git.generalassemb.ly/ArjunRayGA/',
    'https://git.generalassemb.ly/ga-ds-bos/',
    'https://git.generalassemb.ly/ga-wdi-boston/'
]


def check_repo(path):
    repo = Repo(path)
    remote_url =  repo.remotes.origin.url if repo.remotes else ''
    if not any([match in remote_url for match in ghub_origin_match_strings]):
        print crayons.yellow('\n\nNOT INCLUDED:  {}\n{}\nREPO NOT IN YOUR GITHUB ACCOUNTS!\norigin: "{}"\n'.format(path.upper(),'-' * 80, remote_url))
    else:
        active_branch = str(repo.active_branch)
        branches = [str(b) for b in repo.branches if str(b) <> active_branch]
        print crayons.white('\n\n{}\n{}'.format(path.upper(), '-' * 80), bold=True)
        print('active branch: "{}"'.format(active_branch))

        if len(branches) > 0:
            print 'other branches: {}'.format(branches)

        print ('\nchecking "{}"'.format( active_branch))
        try:
            git = repo.git
            status = git.status()
            if 'nothing to commit' not in status:
                print crayons.red(status)
                print ' '
            else:
                print crayons.green('OK!\n')
        except:
            print crayons.red('unable to check branch')

        for branch in branches:
            print '\nattempting to switch to branch "{}" ...'.format(branch)
            try:
                getattr(repo.heads, branch).checkout()

                print ('\nchecking "{}"'.format(branch))
                git = repo.git
                status = git.status()
                if 'nothing to commit' not in status:
                    print crayons.red(status)
                    print ' '                
                else: 
                    print crayons.green('OK!\n')           
            except:
                print crayons.red('unable to check branch')

#                 OK = '''On branch master
# Your branch is up to date with 'origin/master'.

# nothing to commit, working tree clean'''
                # print status, dir(repo)


                # repo_dirs.append(path)
                # repo_settings.append({
                #     'origin': remote_url
                # })


                # print 'git -C "{}" status'.format(path)
                # proc = Popen(['git','status'])
                # # result = proc.communicate()
                # # print result

repo_dirs = []
repo_settings = []
for search_dir in dir_paths:
    for path, dirs, _ in os.walk(os.path.expanduser(search_dir)):
        if '.git' in dirs:
            check_repo(path)


repos = (zip(repo_dirs, repo_settings))

# for path, settings in repos:
#     repo = Repo(path)
#     git = repo.git
#     print repo.branches



# for d, s in repos:
#     print d, s