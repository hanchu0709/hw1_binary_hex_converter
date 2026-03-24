#include "mainwindow.h"  //引入主視窗
#include <QApplication>  //Qt：視窗的GUI應用程式類別

int main (int argc, char *argv[]){
    QApplication a(argc, argv);      //建立應用程式
    Mainwindow w;                    //建立主視窗
    w.show();                        //顯示視窗
    return a.exec();                 //執行
}