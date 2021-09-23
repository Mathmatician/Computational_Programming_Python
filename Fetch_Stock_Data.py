import time
import urllib3

# all time variables defined in seconds
one_minute = 60;
one_hour = 3600;
one_day = 86400;

def GetPrice(stock_tag, days_ago):
    # request variable
    http = urllib3.PoolManager();

    current_time = int(time.time());
    start_time = current_time - days_ago * one_day;

    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_tag + "?period1=" + str(start_time) +"&period2=" + str(current_time) + "&interval=1d&events=history&includeAdjustedClose=true";
    r = http.request('GET', url);
    csv_file = str(r.data);
    csv_file = csv_file.replace("'", "");
    rows = csv_file.split('\\n');

    return GetData(rows, 1);



# 1 = open
# 2 = high
# 3 = low
# 4 = close
# 5 = volume
def GetData(data, type):
    arr = [];
    for i in range(1, len(data)):
        line = data[i];
        line = line.split(',');
        val = float(line[type]);
        arr.append(val);
    
    return arr;
