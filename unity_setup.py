#!/usr/bin/env python
import os
import os.path
import subprocess

from subprocess import Popen, PIPE

def _set_value(plist_path, key, value):
    subprocess.call(['plutil', '-replace', key, '-string', value, plist_path])

def _get_jdk_home():
    proc = Popen(['/usr/libexec/java_home'], stdout=PIPE)
    return proc.communicate()[0].splitlines()[0]

def _get_android_sdk_home():
    base_dir = os.path.expanduser('/usr/local/Cellar/android-sdk')
    options = os.listdir(base_dir)
    return os.path.join(base_dir, max(options))

if __name__ == '__main__':
    file_path = os.path.expanduser('~/Library/Preferences/com.unity3d.UnityEditor5.x.plist')
    _set_value(file_path, 'CacheServerIPAddress', 'cardscachebox')
    _set_value(file_path, 'JdkPath', _get_jdk_home())
    _set_value(file_path, 'AndroidSdkRoot', _get_android_sdk_home())

