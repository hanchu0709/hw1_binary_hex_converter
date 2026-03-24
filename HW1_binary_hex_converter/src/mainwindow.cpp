#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <algorithm>

mainwindow::mainwindow(QWidget *parent)
    :QMainwindow(parent), ui(new ui::mainwindow){
        ui ->setupui(this);
}

mainwindow::~mainwindow(){
    delete ui;
}

//十進位轉成二進位
Qstring mainwindow::dec_to_bin (int dec){
    if (dec == 0)
        return "0";                                //若輸入值為0，輸出0

    Qstring result = "";                           //宣告result字串
    while (dec > 0){
        result = Qchar('0' + (dec % 2)) + result;  //取得輸入值最低位的二進位數字，並轉成字元加入字串
        dec /= 2;                                  //除以2，進入下一位
    }
   std::reverse(result.begin(), result.end());     //將result中的值反轉
    return result;                                 //回傳result           
}

//十進位轉成十六進位
Qstring mainwindow::dec_to_hex(int dec){
    Qstring hex_chars = "0123456789ABCDEF";     //十六進位對應字元
    if (dec == 0)
        return "0";                            //若輸入值為0，輸出0

    Qstring result = "";                        //宣告
    while (dec > 0){
        result = hex_chars[dec % 16] + result ;  //取得餘數0~15，對應十六進位自元
        dec /= 16 ;                              //將數字除以16
    }
    std::reverse(result.begin(), result.end());
    return result;                             //回傳result
}

//二進位轉成十進位
int mainwindow::bin_to_dec (Qstring bin){
    int result = 0;
    for (int i =0; i < bin.length(); i++){   //i的範圍會在0，到bin的長度，且每次都會先賦值使用後再加1
        result = result * 2;                 //將result乘2
        result += (bin[i].toLatin1() - '0'); //加上目前位元的數值
    return result;                           //回傳result
    }
}

//十六進位轉成十進位
int mainwindow::hex_to_dec (Qstring hex){
    int result = 0;
    for (int i = 0; i < hex.length(); i++){
        Qchar c = hex[i];                     //取得目前字元c
        int value;                           //宣告變數value：對應A~F的個位數0~5
        if (c >= '0' && c <= '9')
            value = c.toLatin1() - '0';                 //若c在0~9之間，則value值為0
        else if (c >= 'A' && C <= 'F')
            value = c.toLatin1() - 'A' + 10;            //若c為字母，value便會等於c先減去字母A~F對應0~5，再加10
        else  (c >= 'a' && C <= 'f')         //大小寫差異
            value = c.toLatin1() - 'a' + 10;
        result = result * 16 + value;        //將result乘16再加上value
    return result; 
    }
}

//按鈕
void mainwindow::on_convertButton_clicked()
{
    QString bin = ui->binInput->text();
    QString dec = ui->decInput->text();
    QString hex = ui->hexInput->text();

    if (!bin.isEmpty()) {
        int d = bin_to_dec(bin);
        if (d == -1) {
            ui->decInput->setText("Error");
            return;
        }
        ui->decInput->setText(QString::number(d));
        ui->hexInput->setText(dec_to_hex(d));
    }

    else if (!dec.isEmpty()) {
        int d = dec.toInt();
        ui->binInput->setText(dec_to_bin(d));
        ui->hexInput->setText(dec_to_hex(d));
    }

    else if (!hex.isEmpty()) {
        int d = hex_to_dec(hex);
        if (d == -1) {
            ui->decInput->setText("Error");
            return;
        }
        ui->decInput->setText(QString::number(d));
        ui->binInput->setText(dec_to_bin(d));
    }
}