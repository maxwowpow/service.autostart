import xbmc
import xbmcaddon

target_type = xbmcaddon.Addon().getSetting('target_type')
target = xbmcaddon.Addon().getSetting('target')
wait = xbmcaddon.Addon().getSetting('wait_time')
activate_window_format_string = 'ActivateWindow({0},return)'

xbmc.sleep(int(wait))

if target_type == 'window':
    activate_window_argument = target

elif target_type == 'plugin':
    activate_window_argument =  '10025,plugin://{0}'.format(target)

if activate_window_argument is not None:
    xbmc.executebuiltin(activate_window_format_string.format(activate_window_argument))