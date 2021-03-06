N =eval(input())

dayfactor =1.0

dayup = pow(dayfactor+N/1000,365)
daydown =pow(dayfactor-N/1000,365)
difference = int(dayup//daydown)

print ("{:.2f},{:.2f},{}".format(dayup,daydown,difference))

"""
天天向上的力量 III

描述：

一年365天，以第1天的能力值为基数，记为1.0。

当好好学习时，能力值相比前一天提高N‰；当没有学习时，能力值相比前一天下降N‰。

每天努力或放任，一年下来的能力值相差多少呢？其中，N的取值范围是0到100，N可以是小数，假设输入符合要求。

获得用户输入的N，计算每天努力和每天放任365天后的能力值及能力间比值，其中，能力值保留小数点后2位，能力间比值输出整数，输出结果间采用英文逗号分隔。

使用input()获得N。

示例：
输入
1

输出
1.44,0.69,2 
"""
