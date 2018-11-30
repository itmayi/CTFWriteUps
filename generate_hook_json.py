import json
from pprint import pprint

#with open("/Users/guardianangel/Desktop/test.json") as data_file:
#    data = json.load(data_file)
#pprint(data)

array = []
json_file = {}
count=0
def make(classname,method,obj,type):
    json = {}
    json["class_name"]=classname
    json["method"]=method
    json["thisObject"]=obj
    json["type"]=type
    array.append(json)
    global  count
    count +=1

def sms():
    make("java.lang.reflect.Method", "invoke", False, "reflection")
    make("android.telephony.SmsManager", "sendTextMessage", False, "sms")
    make("android.telephony.SmsManager", "sendMultipartTextMessage", False, "sms")
    make("android.telephony.SmsMessage", "getMessageBody", False, "sms")
    make("android.telephony.SmsManager", "sendDataMessage", False, "sms")
    make("android.telephony.SmsMessage", "createFromPdu", False, "sms")
    make("android.telephony.SmsMessage", "getDisplayMessageBody", False, "sms")
    make("android.telephony.SmsMessage", "getMessageBody", False, "sms")
    make("android.telephony.SmsMessage", "createFromPdu", False, "telephony")
    make("android.telephony.SmsMessage", "getDisplayMessageBody", False, "telephony")
    make("android.telephony.SmsMessage", "getDisplayOriginatingAddress", False, "telephony")
    make("android.telephony.SmsMessage", "getEmailBody", False, "telephony")
    make("android.telephony.SmsMessage", "getEmailFrom", False, "telephony")
    make("android.telephony.SmsMessage", "getIndexOnIcc", False, "telephony")
    make("android.telephony.SmsMessage", "getIndexOnSim", False, "telephony")
    make("android.telephony.SmsMessage", "getMessageBody", False, "telephony")
    make("android.telephony.SmsMessage", "getOriginatingAddress", False, "telephony")
    make("android.telephony.SmsMessage", "getPdu", False, "telephony")
    make("android.telephony.SmsMessage", "getProtocolIdentifier", False, "telephony")
    make("android.telephony.SmsMessage", "getPseudoSubject", False, "telephony")
    make("android.telephony.SmsMessage", "getServiceCenterAddress", False, "telephony")
    make("android.telephony.SmsMessage", "getStatus", False, "telephony")
    make("android.telephony.SmsMessage", "getStatusOnIcc", False, "telephony")
    make("android.telephony.SmsMessage", "getStatusOnSim", False, "telephony")
    make("android.telephony.SmsMessage", "getSubmitPdu", False, "telephony")
    make("android.telephony.SmsMessage", "getUserData", False, "telephony")
    # make("android.content.ContentResolver", "query", False, "content")

def crypto():
    make("android.util.Base64", "encode", False, "crypto")
    make("android.util.Base64", "encodeToString", False, "crypto")
    make("javax.crypto.spec.SecretKeySpec", None, False, "crypto")
    make("javax.crypto.Cipher", "doFinal", True, "crypto")
    make("javax.crypto.Mac", "doFinal", False, "crypto")

def dex():
    make("dalvik.system.BaseDexClassLoader", "findResource", False, "dex")
    make("dalvik.system.BaseDexClassLoader", "findLibrary", False, "dex")
    make("dalvik.system.DexFile", "loadDex", False, "dex")
    make("dalvik.system.DexClassLoader", None, False, "dex")
    make("dalvik.system.BaseDexClassLoader", "findResources", False, "dex")
    make("dalvik.system.DexFile", "loadClass", False, "dex")
    make("dalvik.system.DexFile", None, False, "dex")
    make("dalvik.system.PathClassLoader", None, False, "dex")


def fingerprint():
    make("android.telephony.TelephonyManager", "getDeviceId", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getSubscriberId", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getLine1Number", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getNetworkOperator", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getNetworkOperatorName", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getSimOperatorName", False, "fingerprint")
    make("android.net.wifi.WifiInfo", "getMacAddress", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getSimCountryIso", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getSimSerialNumber", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getNetworkCountryIso", False, "fingerprint")
    make("android.telephony.TelephonyManager", "getDeviceSoftwareVersion", False, "fingerprint")
    make("android.os.Debug", "isDebuggerConnected", False, "fingerprint")

def mail():
    make("java.util.Properties", "put", False, "system")
    make("javax.mail.Transport", "send", False, "binder")
    make("javax.mail.Transport", "sendMessage", False, "binder")
    make("javax.mail.Transport", "connect", False, "binder")
    make("javax.mail.internet.InternetAddress", "init", False, "binder")
    make("android.content.Intent", None, False, "binder")
    make("android.content.Intent", "hasExtra", False, "binder")
    make("android.content.Intent", "parseUri", False, "binder")
    make("android.content.Intent", "putExtra", False, "binder")
    make("android.content.Intent", "setAction", False, "binder")
    make("android.content.Intent", "setClass", False, "binder")
    make("android.content.Intent", "setClassName", False, "binder")
    make("android.content.Intent", "setData", False, "binder")
    make("java.net.URI", "parse", False, "network")

def query():
    make("android.content.ContentResolver", "query", False, "content")
    make("android.content.ContentResolver", "delete", False, "content")
    make("android.content.ContentResolver", "query", False, "content")
    make("android.content.ContentResolver", "delete", False, "content")
    make("android.content.ContentResolver", "acquireContentProviderClient", False, "content")
    make("android.content.ContentResolver", "acquireUnstableContentProviderClient", False, "content")
    make("android.content.ContentResolver", "addPeriodicSync", False, "content")
    make("android.content.ContentResolver", "applyBatch", False, "content")
    make("android.database.sqlite.SQLiteCursor", "getDatabase", False, "content")
def file():
    make("libcore.io.IoBridge", "open", False, "file")
    make("android.app.SharedPreferencesImpl$EditorImpl", "putString", False, "file")
    make("android.app.SharedPreferencesImpl$EditorImpl", "putBoolean", False, "file")
    make("android.app.SharedPreferencesImpl$EditorImpl", "putInt", False, "file")
    make("android.app.SharedPreferencesImpl$EditorImpl", "putLong", False, "file")
    make("android.app.SharedPreferencesImpl$EditorImpl", "putFloat", False, "file")
    make("android.content.ContentValues", "put", False, "file")
    make("android.content.SharedPreferences.Editor", "remove", False, "file")

    make("java.io.File", None, False, "file")
    make("java.io.File", "createNewFile", False, "file")
    make("java.io.File", "createTempFile", False, "file")
    make("java.io.File", "delete", False, "file")
    make("java.io.File", "list", False, "file")
    make("java.io.File", "listFiles", False, "file")
    make("java.io.File", "listRoots", False, "file")
    make("java.io.File", "renameTo", False, "file")

    make("android.content.ContextWrapper", "deleteFile", False, "file")
    make("android.content.ContextWrapper", "fileList", False, "file")

    make("android.net.URI.HierachicalURI", "create", False, "file")
    make("android.net.URI.HierachicalURI", "resolve", False, "file")

    make("java.net.URI", "create", False, "file")
    make("java.net.URI", "resolve", False, "file")



def network():
    make("java.net.HttpURLConnection", None, False, "network")
    make("javax.net.ssl.SSLContext", "init", False, "network")
    make("android.net.SSLCertificateSocketFactory", None, False, "network")
    make("android.net.SSLCertificateSocketFactory", "getDefault", False, "network")
    make("android.net.SSLCertificateSocketFactory", "createSocket", False, "network")
    make("android.net.SSLCertificateSocketFactory", "getHttpSocketFactory", False, "network")
    make("android.net.SSLCertificateSocketFactory", "getNpnSelectedProtocol", False, "network")
    make("android.net.SSLCertificateSocketFactory", "setHostname", False, "network")
    make("android.net.SSLCertificateSocketFactory", "setKeyManager", False, "network")
    make("android.net.SSLCertificateSocketFactory", "setNpnProtocols", False, "network")
    make("android.net.SSLCertificateSocketFactory", "setTrustManagers", False, "network")
    make("android.net.SSLCertificateSocketFactory", "setUseSessionTickets", False, "network")

    make("java.net.ServerSocket", None, False, "network")
    make("java.net.ServerSocket", "accept", False, "network")
    make("java.net.ServerSocket", "bind", False, "network")

    make("java.net.Proxy", "Proxy", False, "network")

    make("java.net.Socket", None, False, "network")
    make("java.net.Socket", "bind", False, "network")
    make("java.net.Socket", "connect", False, "network")

    make("org.apache.http.client.methods.HttpGet", None, False, "network")
    make("org.apache.http.client.methods.HttpGet", "getMethod", False, "network")
    make("org.apache.http.client.methods.HttpGet", "getURI", False, "network")

    make("org.apache.http.impl.client.AbstractHttpClient", "execute", False, "network")

    make("java.net.HttpURLConnection", "connect", True, "network")
    make("java.net.HttpURLConnection", "getContent", False, "network")
    make("java.net.HttpURLConnection", "getURL", False, "network")
    make("java.net.HttpURLConnection", "setRequestProperty", False, "network")
    make("java.net.HttpURLConnection", "getInputStream", True, "network")
    make("java.net.HttpURLConnection", "getOutputStream", True, "network")
    make("java.net.HttpURLConnection", "getResponseCode", True, "network")

    make("java.net.URL", None, False, "network")
    make("java.net.URL", "getAuthority", False, "network")
    make("java.net.URL", "getContent", False, "network")
    make("java.net.URL", "getDefaultPort", False, "network")
    make("java.net.URL", "getHost", False, "network")
    make("java.net.URL", "getPort", False, "network")
    make("java.net.URL", "openConnection", False, "network")
    make("java.net.URL", "toURI", False, "network")

    make("libcore.io.IoBridge", "recvfrom", False, "network")
    make("libcore.io.IoBridge", "sendto", False, "network")
    make("libcore.io.IoBridge", "connectErrno", False, "network")
    make("libcore.io.IoBridge", "connect", False, "network")
    make("libcore.io.IoBridge", "bind", False, "network")

    make("android.webkit.WebView", "addJavascriptInterface", False, "network")
    make("android.webkit.WebView", "capturePicture", False, "network")
    make("android.webkit.WebView", "clearSslPreferences", False, "network")
    make("android.webkit.WebView", "evaluateJavascript", False, "network")
    make("android.webkit.WebView", "findAddress", False, "network")
    make("android.webkit.WebView", "loadData", False, "network")
    make("android.webkit.WebView", "loadDataWithBaseURL", False, "network")
    make("android.webkit.WebView", "loadUrl", False, "network")
    make("android.webkit.WebView", "postUrl", False, "network")
    make("android.webkit.WebView", "setCertificate", False, "network")
    make("android.webkit.WebView", "setHttpAuthUsernamePassword", False, "network")


def other():
    make("android.app.ApplicationPackageManager", "getInstalledPackages", False, "content")
    make("android.app.ActivityManager", "killBackgroundProcesses", False, "runtime")
    make("android.os.Process", "killProcess", False, "runtime")
    make("java.lang.Runtime", "exec", False, "runtime")
    make("java.lang.ProcessBuilder", "start", True, "runtime")
    make("java.lang.reflect.Method", "invoke", False, "reflection")
    make("android.app.ApplicationPackageManager", "setComponentEnabledSetting", False, "generic")
    #android.app.admin.DevicePolicyManager.isAdminActive
    make("android.app.admin.DevicePolicyManager", "isAdminActive", False, "generic")
    make("android.app.admin.DeviceAdminReceiver", "onReceive", False, "generic")
    make("android.content.ContextWrapper", "sendBroadcast", False, "binder")
    make("android.app.ActivityManager", "getRunningAppProcesses", False, "system")
    make("android.app.ActivityManager", "getRunningServiceControlPanel", False, "system")
    make("android.app.ActivityManager", "getRunningServices", False, "system")
    make("android.app.ActivityManager", "getRunningTasks", False, "system")
    make("android.net.ConnectivityManager", "getNetworkInfo", False, "system")
    make("com.android.server.pm.PackageManagerService", "installPackageWithVerificationAndEncryption", False, "system")
    make("com.android.server.pm.PackageManagerService", "installPackageLI", False, "system")
    make("android.content.ContextWrapper", "startActivity", False, "binder")
    make("android.content.BroadcastReceiver", "onReceive", False, "binder")
    make("java.lang.Thread", "start", False, "binder")
    make("java.util.zip.ZipFile", "getInputStream", False, "binder")
    make("java.util.zip.ZipFile", "entries", False, "binder")
    make("java.util.zip.ZipFile", "getEntry", False, "binder")

sms()
crypto()
dex()
fingerprint()
mail() #error
query() #error
file()
network()
other()

print count





json_file["hookConfigs"]=array
json_file["trace"]=False
with open('hooks.json', 'w') as outfile:
    json.dump(json_file, outfile ,sort_keys = True, indent = 4,ensure_ascii=False)