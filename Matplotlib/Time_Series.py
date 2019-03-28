x = input()
y = input()
z = input()

li_group1 = ['appserver1','appserver2']
li_group2 = ['appserver1','appserver2','appserver3']

x_sp = x.split()
y_sp = y.split()
z_sp = z.split()
#print(x_sp)
li_group_agg = list()
li_group_aggr = list()

for i in range(len(li_group1)):
    if(x_sp[0] == li_group1[i]):
        li_group_agg.append(x_sp)
    if(y_sp[0] == li_group1[i]):
        li_group_agg.append(y_sp)
    if(z_sp[0] == li_group1[i]):
        li_group_agg.append(z_sp)


for j in range(len(li_group2)):
    if(x_sp[0] == li_group2[j]):
        li_group_aggr.append(x_sp)
    if(y_sp[0] == li_group2[j]):
        li_group_aggr.append(y_sp)
    if(z_sp[0] == li_group2[j]):
        li_group_aggr.append(z_sp)

print(li_group_agg)
print(li_group_aggr)

li_group1_agg = list()
li_group2_agg = list()
li_group1_agg.append('group1')
li_group2_agg.append('group2')
t_add = 0
fault = 0
load = 0
for i in range(len(li_group_agg)):
    t_add = t_add+int(li_group_agg[i][1])
    fault = fault+int(li_group_agg[i][2])
    load  = load+int(li_group_agg[i][3])
li_group1_agg.append(str(t_add))
li_group1_agg.append(str(fault/len(li_group_agg)))
li_group1_agg.append(str(load/len(li_group_agg)))

print(li_group1_agg)

t_group2 = 0
faultg = 0
loadg = 0
for j in range(len(li_group_aggr)):
    t_group2 = t_group2+int(li_group_aggr[j][1])
    faultg = faultg+int(li_group_aggr[j][2])
    loadg  = loadg+int(li_group_aggr[j][3])
li_group2_agg.append(str(t_group2))
li_group2_agg.append(str(faultg/len(li_group_aggr)))
li_group2_agg.append(str(loadg/len(li_group_aggr)))

print(li_group2_agg)

res_group1 = ' '.join(li_group1_agg)
res_group2 = ' '.join(li_group2_agg)

print(res_group1)
print(res_group2)