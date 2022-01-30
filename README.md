# smzdm
什么值得买模拟登陆,签到,非selenium,fork from [yaodi962464/smzdm](https://github.com/yaodi962464/smzdm/tree/master/zhangdama). 做了点简单的优化

1) 使用了 https://github.com/Kevin-Cherish/geetest 的极验破解代码  
2) 抓包获取 RSA的公钥破解  
3) 将 sampleuser.json 更名为 user.json，在user.json 中输入用户名和密码，可以输入多个一起签到，省心省力。  

依赖打包在requestment.txt，输入pip3 install -r requestment.txt即可