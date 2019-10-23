# ShoxieAGod
![Jenkins](https://img.shields.io/jenkins/build/http/47.100.44.59:8081/job/ShoxieAGod/job/master)

基于[noneBot](https://nonebot.cqp.moe)的QQ机器人，可用来查询CSGO战绩

## 使用

不想自己自己部署的话可以尝试已部署的机器人QQ：3308423285

## 已实现功能
- bind [arg]
    
  - 参数
  
    arg: 5e当前用户名
  - 功能

    绑定5e账号到发送信息的QQ号
- history [arg] 
  - 参数
  
    arg: 5e当前用户名，bind后可省略该参数
  - 功能
  
    查询玩家在5e平台的最近10场比赛胜负情况
- recent [arg] 
  - 参数
  
    arg: 5e当前用户名，bind后可省略该参数
  - 功能

    查询玩家在5e平台最近一场比赛的表现
- me [arg] 
  - 参数
  
    arg: 5e当前用户名，bind后可省略该参数
  - 功能

    查询玩家在5e平台最近一个赛季的总体表现

- compare [arg1] [arg2]
  - 参数
  
    arg1： 5e账号初始名
    
    arg2： 5e账号初始名
  - 功能

    对比两个玩家在5e平台最近一个赛季的总体表现
    
## 待完成
- [x] 自动同意进群请求 
- [x] 增加数据库，支持存储qq号对应的5e账号
- [ ] 接入简单的NLP模块，不用指定命令查询
- [ ] 支持查询steam官匹数据
- [ ] 代码重构，测试覆盖