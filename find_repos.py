import crayons
import os
from git import Repo
from subprocess import Popen


# class FindRepos:
#     def __init__(self, dir_paths, match_strings):
#         self.dir_paths = dir_paths
#         self.match_strings = match_strings

#     def traverse_tree(self):
#         for search_dir in self.dir_paths:
#             full_path = os.path.expanduser(search_dir)
#             for path, dirs, _ in os.walk(full_path):
#                 if '.git' in dirs:
#                     RepoCheck(path)



# class RepoCheck:
#     def __init__(self, path):
#         self.path = path
#         self.repo = Repo(path)
#         self.remote_url = self.repo.remotes.origin.url if self.repo.remotes else ''
#         self.check_repo()
        

#     def check_repo(self):
#         if not any([match in remote_url for match in ghub_origin_match])




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

def traverse_tree(dir_paths, match_strings):

    for search_dir in dir_paths:
        for path, dirs, _ in os.walk(os.path.expanduser(search_dir)):
            if '.git' in dirs:
                check_repo(path)


if __name__ == '__main__':
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

    traverse_tree(dir_paths, ghub_origin_match_strings)
