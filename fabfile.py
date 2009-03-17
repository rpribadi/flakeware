def production() :   
    config.fab_user = 'rpribadi'
    config.fab_password = '692a1353'
    config.fab_hosts = ['flakeware.com']
    config.project_dir = '/home/rpribadi/webapps/flakeware_app'
    config.project = 'flakeware'
    config.wsgi = 'wsgi'

def clone():
    require('project_dir',provided_by=[production])
    require('project',provided_by=[production])
    local("echo initial clone")
    run("cd $(project_dir)/; git clone git://github.com/rpribadi/flakeware.git;")
    
def syncdb():
    require('project_dir',provided_by=[production])
    require('project',provided_by=[production])
    local("echo sync database")
    run("python $(project_dir)/$(project)/manage.py syncdb")
    
def update():
    require('project_dir',provided_by=[production])
    require('project',provided_by=[production])
    require('wsgi',provided_by=[production])

    local("echo connecting to server for updating git")
    run("cd $(project_dir)/$(project)/; git reset --hard")
    run("cd $(project_dir)/$(project)/; git pull origin master")
    run("cp $(project_dir)/$(project)/myproject.wsgi $(project_dir)/myproject.wsgi")

def restart():
    local("echo restarting server")
    run("$(project_dir)/apache2/bin/restart")

def set_permission():
    require('project_dir',provided_by=[production])
    require('project',provided_by=[production])

    local("echo changing folder permission on media")
    sudo("chmod -R 777 $(project_dir)/$(project)/media/uploads/")


