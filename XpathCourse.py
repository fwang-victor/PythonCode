#选取节点
'''
XPath使用路径表达式在XML文档中选取节点。节点是通过沿着路径或者step来选取的。
nodename 选取此节点的所有子节点
/        从根节点选取
//       从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
.        选取当前节点
..       选取当前节点的父节点
@        选取属性
属性多值匹配：如果属性有多个值，就需要contains()函数 contain(@class,'li')
'''
#谓语
'''
谓语是用来查找某个特定的节点或者包含某个特定值的节点
谓语被嵌套在方括号中
'''
#选取未知节点
'''
*      匹配任何元素节点
@*     匹配任何属性节点
node() 匹配任何类型的节点
''' 
#选取若干路径
''' 通过在路径表达式中使用"|" 运算符，可以选取若干个路径'''
#获取文本
'''
调用text()方法
如果我们要想获取子孙节点内部的所有文本，可以直接用 // 加 text() 的方式获取，这样可以保证获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。
如果我们想获取某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，然后再调用 text() 方法获取其内部文本，这样可以保证获取的结果是整洁的。
'''