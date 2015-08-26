#!/usr/bin/env python
import os
import os.path
import subprocess

from subprocess import Popen, PIPE

def _set_string_value(plist_path, key, value):
    subprocess.call(['plutil', '-replace', key, '-string', value, plist_path])

def _set_int_value(plist_path, key, value):
    subprocess.call(['plutil', '-replace', key, '-integer', value, plist_path])

def _get_jdk_home():
    proc = Popen(['/usr/libexec/java_home'], stdout=PIPE)
    return proc.communicate()[0].splitlines()[0]

def _get_android_sdk_home():
    base_dir = os.path.expanduser('/usr/local/Cellar/android-sdk')
    options = os.listdir(base_dir)
    return os.path.join(base_dir, max(options))

def _invalidate_plist_cache(plist_path):
    subprocess.call(['defaults', 'read', plist_path])

def _check_unity_not_running():
    unity_running = not subprocess.call(['pgrep', 'Unity$'])
    if unity_running:
        raise Exception("Unity can't be running when this script is run")


if __name__ == '__main__':
    _check_unity_not_running()
    plist_path = os.path.expanduser('~/Library/Preferences/com.unity3d.UnityEditor5.x.plist')
    _set_string_value(plist_path, 'CacheServerIPAddress', 'cardscachebox')
    _set_int_value(plist_path, 'CacheServerEnabled', 1)
    _set_string_value(plist_path, 'JdkPath', _get_jdk_home())
    _set_string_value(plist_path, 'AndroidSdkRoot', _get_android_sdk_home())
    _invalidate_plist_cache(plist_path)

