import matplotlib.container as mc
def cat_vis(x,hue):
    plt.figure(figsize=(12,5))
    g_t = []
    ax = sns.countplot(data=train,x=x,hue=hue,palette='mako',width=0.5)
    for i in range(train[ax.get_legend().get_title().get_text()].nunique()):
        for j in range(train[ax.get_xlabel()].nunique()):
            globals()['__' + str(i) + str(j)] =  int(str(plt.bar_label(ax.containers[i])[j]).split("'")[1])
            g_t.append(globals()['__' + str(i) + str(j)])

    labels = [mc.Container.get_label(ax.containers[x]) for x in range(train[ax.get_legend().get_title().get_text()].nunique())]
    titles = [str(ax.get_xticklabels()[x]).split("'")[1] for x in range(train[ax.get_xlabel()].nunique())]
    total = [sum(g_t[x::len(g_t)//2]) for x in range(train[ax.get_xlabel()].nunique())]
    data = [g_t[x::len(g_t)//2] for x in range(train[ax.get_xlabel()].nunique())]
    color = sns.color_palette('pastel')
    plt.figure(figsize=(18,10))
    ax1 = plt.subplot2grid((train[ax.get_xlabel()].nunique(),2),(0,0))
    plt.pie(total,labels=titles,autopct='%0.2f%%',colors=color)
    plt.title(ax.get_xlabel())
    ax1 = plt.subplot2grid((train[ax.get_xlabel()].nunique(),2),(0,1))
    grand_labels = [x+" & " +y for x in labels for y in titles]
    plt.pie(g_t,labels=grand_labels,autopct='%0.2f%%',colors=color)
    plt.title('Corelation')
    t,j = 1,0
    for i in range(train[ax.get_xlabel()].nunique()):
        if j == 2:
            t+=1
            j = 0
        ax1 = plt.subplot2grid((train[ax.get_xlabel()].nunique(),2),(t,j))
        plt.title(titles[i])
        plt.pie(data[i],labels=labels, autopct='%0.2f%%',colors=color)
        j+=1
    plt.show()