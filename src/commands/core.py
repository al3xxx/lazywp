#!/usr/bin/python3

import json

def config():
    return {
        'label': 'Core',
        'menu': 'Core',
        'actions': [
            ['v', 'core_version', 'Get WP core version'],
            ['V', 'core_verify', 'Verify WP core files checksums'],
            ['R', 'core_refresh', 'Force reinstall core while keeping content'],
        ],
        'statusbar': [
            'v: version',
            'V: verify',
            'R: reinstall',
        ]
    }

def install_plugin(lazywp, data):
    '''
    Asks a user for a plugin which needs to be installed

    Parameters:
        lazywp (obj): the lazywp object
        data (dict): the transfer data dict

    Returns:
        void
    '''
    plugin = lazywp.slinputbox([f"Please enter the slug of the plugin you want to install"])
    lazywp.msgbox([f"Downloading plugin {plugin}"])
    lazywp.wp(f"plugin install {plugin}", False)
    lazywp.reload_content = True
 

def deinstall_plugin(lazywp, data):
    '''
    Deinstalls a plugin

    Parameters:
        lazywp (obj): the lazywp object
        data (dict): the transfer data dict

    Returns:
        void
    '''

    result = lazywp.askbox([f"Are you sure you want to delete {data['active_plugin']['name']}?"])
    if result == True:
        lazywp.reload_content = True
        lazywp.cursor_position = 0
        lazywp.msgbox([f"Deleting plugin {data['active_plugin']['name']}"])
        lazywp.wp(f"plugin delete {data['active_plugin']['name']}", False)

def update_plugin(lazywp, data):
    '''
    Updates a plugin

    Parameters:
        lazywp (obj): the lazywp object
        data (dict): the transfer data dict

    Returns:
        void
    '''
    lazywp.reload_content = True
    lazywp.msgbox([f"Updating plugin {data['active_plugin']['name']}"])
    lazywp.wp(f"plugin update {data['active_plugin']['name']}", False)

