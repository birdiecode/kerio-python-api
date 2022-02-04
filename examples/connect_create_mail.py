from kerio import KerioConnect

kc = KerioConnect("server.adr", "user@domain", "password")
kc_ap = KerioConnectToolAccessPolicy(kc.getGroupListAccessPolicy()['groups']).getDefault()
kc_d =  KerioConnectToolDomains(kc.getDomains()['list']).get("domain")
ul = [KerioConnectToolMakeUser("fullname", "nikename", "desc", kc_d, kc_ap, "password").skeleton]
print(kc.createUsers(ul))

