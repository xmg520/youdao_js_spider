# 基于有道云翻译的简单破解JS加密

### 项目实现，通过JS解密实现对有道翻译的反爬虫操作
####关键js代码：
```javascript
 var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        }
    };
```
####知识点：
```javascript
chrome开发者工具调试操作
hashlib加密操作
```

### 参考文档
[宝藏up视频](https://www.bilibili.com/video/BV13A411b74e)  
[文档](https://blog.csdn.net/July_whj/article/details/81588856)

### 最后
根据思路快速淦了个demo出来，  
虽然所有代码都有注释，但是没有按照模块化来编写代码啦，  
如果对美观有要求的盆友我也为你们找到一个模块化的Demo --> [点击参观](https://github.com/lyren123/YoudaoTranslate/blob/master/YoudaoTranslate.py)
