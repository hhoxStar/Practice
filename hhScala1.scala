import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by samsung on 2018/7/20.
  */
object hhScala1 {
 def main(args:Array[String])  {//main方法
 println("hello scala")
 System.out.println("hello world")
   val a=3//int
   val b=3.0f//float
   val c=3.9d//double
   val d="你好"//string
   val e="a"//char
   val f=true//boolean
   val a1=Array(1,2,4,-8,10)//数组类型Array==List
   val a2=Array(1,2,4,"a","b")
   val a3=Array[Int](1,2,9)
   val b1=List[Int](1,2,3,10,11,3)//List列表类型   [1,2,3,4....]  a[0]
   val b2=List[String]("a","b","abce")
   val b3=Tuple2(1,2)//元组类型，里面限定变两个数
   val b4=Tuple2("1","2")//没有类型限制
   //打印元素
   println(a,b,c)
   //获取元素
   println(b1(2))
   println("列表b1的第三个元素："+b1(2))//3
   println("元组b3的第一个第二个元素："+b3._1+","+b3._2)
 }
}


object hhScala2 {
  def main(args:Array[String])  {//main方法
    println("hello scala")
    System.out.println("hello world")
    val a:Int=3//int
    val b:Float=3.0f//float
    val c:Double=3.9d//double
    val d:String="你好"//string
    val e:Char='a'//char
    val f:Boolean=true//boolean
    val a1:Array[Int]=Array(1,2,4,-8,10)//数组类型Array==List....,,水果！=苹果
    val a2:Array[Any]=Array(1,2,4,"a","b")
    val a3:Array[Int]=Array[Int](1,2,9)
    val b1:List[Int]=List[Int](1,2,3,10,11,3)//List列表类型   [1,2,3,4....]  a[0]
    val b2:List[String]=List[String]("a","b","abce")
    val b3:Tuple2[Int,Int]=Tuple2(1,2)//元组类型，里面限定变两个数
    val b4:Tuple2[String,String]=Tuple2("1","2")//没有类型限制
    //打印元素
    println(a,b,c)
    //获取元素
    println(b1(2))
    println("列表b1的第三个元素："+b1(2))//3
    println("元组b3的第一个第二个元素："+b3._1+","+b3._2)
    ///////////////////////////////////////占位符%s
   println( "今天温度是%s".format(38))
  }


}



object hhScalaDict3{
  def main(args:Array[String]) {
    //dict Map
    val a=Map("name"->"爱酱","AI"->List("二次元","偶像"))//{"name":"爱酱"}
    //a['name']   a("name")
    println(a("name"))
    println(a("AI"))
    val b=Map(("name","爱酱"),("AI",List("二次元","偶像")))
    println(b("name"))
    println(b("AI"))

  }
}



object hhScalaIf4 {
  def main(args: Array[String]) {
//或者不选，二选一，多选一
    if(true){
      println("选择")
    }
    if(1>2){
      println("1>2")
    }else{
      println("1<2")
    }
    //////////
    var score=90
    if(score>=90){
      println("A")
    }else if(score>=80){
      println("B")
    }else if(score>=60){
      println("c")
    }else{
      println("D")
    }
  }
}

object hhScalaIf5 {
  def main(args: Array[String]){
    val ls=List("a","b","c","d")
    println(ls.length)
    for(i <-ls){
      println(i)
    }
    while(true){
      println("无限循环")
    }
  }
  }

///for升级
object hhScala3 {
  def main(args: Array[String]): Unit = {
    println("for循环的升级 if搭配")
    ////////////////////////for循环的升级 if搭配..快捷键 查看函数说明ctrl+p
    for (i <- Range(0, 10) if (i > 5)) {
      ////break,continue
      println(i)
    }
    println("for和yield很搭")
    /////for和yield很搭
    val fun1 = for (i <- Range(0, 10)) i * 10 - 1
    println(fun1)
    val fun2 = for (i <- Range(0, 10)) yield i * 10 - 1
    println("fun2:" + fun2)
    import scala.util.control.Breaks._
    /////语句控制————导入工具包导入Breaks下的所有的功能
    //break()
    for (i <- Range(0, 10)) {
      if (i == 3) {
        break()
      }
      println("break" + i)
    }
    println("----------")
  }
}

  ////练习9 Scala题目
  //1.定义一个天气温度表，写出里面每一天的温度
  //2.打印一周的天气，天气里面的周三打印例外：周三+温度
  object hhScala4 {
    def main(args: Array[String]) {
      var a: List[Int] = List(21, 24, 23, 22, 21, 27, 25, 26)
      println("一周的温度")
      var b = Array(1, 2, 3, 4, 5, 6, 7)
      for (i <- b) {
        if (i == 3) {
          println("周三" + a(3) + "\t")
        }
        else {
          println(a(i) + "\t")
        }
      }
    }
  }


////函数语法123
/*函数
  *函数语法1
  * def  函数名(变量：类型...):返回类型=｛
  *   指令的集合
  *   ｝
  *函数语法2（lambda）
  * (变量：类型。。）=>一个值
  *函数语法3（指令的集合中只有一条语句）
  * def 函数名（变量：类型）[:类型]=一条语句
 */
object hhScalaFun{
    //
  //
  def main(args:Array[String]): Unit ={
    println("main...")
    def sum(a:Int,b:Int):Int={
      a+b//return a+b
    }
    println(sum(3,4))
    //////匿名函数（lambda函数 一句话函数）闭包
    val add=(a:Int,b:Int)=>a+b//return a+b
    println("lanbda函数："+add(3,4))
    def ride(a:Int,b:Int):Int=a+b
    println("指令的集合只有一条指令的函数："+ride(3,4))
    println("含有默认值的函数参数：")
    def abc(a:Int,b:Int,opt:String="+"):Int={
      println(opt)
      a+b
    }
    abc(3,4)
    abc(3,4,"-")
  }
}


object hhScala5{
def main(args:Array[String]): Unit = {
  //1到10 每个数*10 打印每个数
  //  for(i<-Range(1,11)){
  // val j=i*10
  // println(j)
  // }
  ////使用函数式编写的思想写出以上的要求,,,,, 闭包lambda+函数作为参数
  /// def m(i:Int)=i*10
  1.to(10).map(i => i * 10).foreach(i => println(i)) //lambda 函数作为了第一等公民（参数）传递

}
}






object YqScalaFun2{
  def main(args: Array[String]) {
    //1到10 每个数*10 打印每个数
    //    for(i<-Range(1,11)){
    //      val j=i*10
    //      println(j)
    //    }
    //使用函数式编写的思想写出以上的要求,, ,,,闭包lambda+函数作为参数
    //    def m(i:Int)=i*10
    1.to(10).map(i=>i*10).foreach(i=>println(i))//lambda函数作为了第一等公民(参数) 传递
  }
}

object YqScalaXml{
  def main(args: Array[String]) {
    val xml = <ul class="clearfix">
      <li data-val="北京" data-id="2" onclick="$.setVar('claimCity', 11)">北京</li>
      <li data-val="天津" data-id="2" onclick="$.setVar('claimCity', 12)">天津</li>
      <li data-val="河北" data-id="2" onclick="$.setVar('claimCity', 13)">河北</li>
      <li data-val="山西" data-id="2" onclick="$.setVar('claimCity', 14)">山西</li>
      <li data-val="内蒙古" data-id="2" onclick="$.setVar('claimCity', 15)">内蒙古</li>
      <li data-val="辽宁" data-id="2" onclick="$.setVar('claimCity', 21)">辽宁</li>
      <li data-val="吉林" data-id="2" onclick="$.setVar('claimCity', 22)">吉林</li>
      <li data-val="黑龙江" data-id="2" onclick="$.setVar('claimCity', 23)">黑龙江</li>
      <li data-val="上海" data-id="2" onclick="$.setVar('claimCity', 31)">上海</li>
      <li data-val="江苏" data-id="2" onclick="$.setVar('claimCity', 32)">江苏</li>
      <li data-val="浙江" data-id="2" onclick="$.setVar('claimCity', 33)">浙江</li>
      <li data-val="安徽" data-id="2" onclick="$.setVar('claimCity', 34)">安徽</li>
      <li data-val="福建" data-id="2" onclick="$.setVar('claimCity', 35)">福建</li>
      <li data-val="江西" data-id="2" onclick="$.setVar('claimCity', 36)">江西</li>
      <li data-val="山东" data-id="2" onclick="$.setVar('claimCity', 37)">山东</li>
      <li data-val="河南" data-id="2" onclick="$.setVar('claimCity', 41)">河南</li>
      <li data-val="湖北" data-id="2" onclick="$.setVar('claimCity', 42)">湖北</li>
      <li data-val="湖南" data-id="2" onclick="$.setVar('claimCity', 43)">湖南</li>
      <li data-val="广东" data-id="2" onclick="$.setVar('claimCity', 44)">广东</li>
      <li data-val="广西" data-id="2" onclick="$.setVar('claimCity', 45)">广西</li>
      <li data-val="海南" data-id="2" onclick="$.setVar('claimCity', 46)">海南</li>
      <li data-val="重庆" data-id="2" onclick="$.setVar('claimCity', 50)">重庆</li>
      <li data-val="四川" data-id="2" onclick="$.setVar('claimCity', 51)">四川</li>
      <li data-val="贵州" data-id="2" onclick="$.setVar('claimCity', 52)">贵州</li>
      <li data-val="云南" data-id="2" onclick="$.setVar('claimCity', 53)">云南</li>
      <li data-val="西藏" data-id="2" onclick="$.setVar('claimCity', 54)">西藏</li>
      <li data-val="陕西" data-id="2" onclick="$.setVar('claimCity', 61)">陕西</li>
      <li data-val="甘肃" data-id="2" onclick="$.setVar('claimCity', 62)">甘肃</li>
      <li data-val="青海" data-id="2" onclick="$.setVar('claimCity', 63)">青海</li>
      <li data-val="宁夏" data-id="2" onclick="$.setVar('claimCity', 64)">宁夏</li>
      <li data-val="新疆" data-id="2" onclick="$.setVar('claimCity', 65)">新疆</li>
    </ul>
    xml.child.foreach(node=>{
      val value = node.attribute("onclick")
      //      println(value)
      if(value!=None){
        //012
        //$.setVar('claimCity', 11)
        //        println(value.get.toString())
        val a = value.get.toString().split(", ")(1).substring(0,2)
        println(a)
      }
    })
  }
}
object tes{
  def main(args: Array[String]) {
    println("$.setVar('claimCity', 11)".split(", ")(1))
    val a = "$.setVar('claimCity', 11)".split(", ")(1).substring(0,2)
    println(a)
  }
}


/**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  */


/*练习11:可视化展示
1.获取学校名
2.获取学校招生人数
3.在Echarts展示
*/
object hhSpark1{
  def main(args:Array[String]) {
    //sparkcontext的配置，运行在本地 名称为cala
    import org.json.JSONObject//导入str转json工具包
    import org.apache.spark.SparkConf//
    import org.apache.spark.SparkContext
    import scala.collection.mutable.ListBuffer
    //sparkcontext的配置，运行在本地，名称为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local").set("spark.testing.memory", "2147480000")
    val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
    //使用spark读取文本文件
    sc.textFile("湖北学校.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{//line str===>List line  抚平
      val  json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        //        jsonlist.getJSONObject(0)
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))

  }
}


object hhSparkTest{
  def main(args:Array[String]): Unit ={
    import scala.collection.mutable.ListBuffer
    println("aaa@qq.com".endsWith("qq.com"))
    println("status\":1")
    //new JsonObject
    //import json
    import org.json.JSONObject
    val json = new JSONObject("{\"data\":{\"city_name\":\"\\u6e56\\u5357\"},\"info\":\"\",\"status\":0}")
    println(json.getInt("status"))
    println(json.getJSONObject("data"))
    val list = List[Int](1,1,1)//大小不变的固定列表
    //    list(2) = 3
    val list2 = ListBuffer[Int]()
    list2.append(3)
    list2.append(4)
    println(list2)
  }
}

/*
     //   练习题11：2300学校招生人数echarts可视化展示
          西南大学,8888
        重庆理工大学,5555
        ================
        data: ['巴西','印尼','美国','印度','中国','世界人口(万)']
        data: [1932, 23438, 31000, 121594, 13411, 681807]

        =====
        html,css,javascript,jquery,ajax
        echarts,json,xml
*/



