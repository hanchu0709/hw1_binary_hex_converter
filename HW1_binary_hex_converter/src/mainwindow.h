#ifndef MAINWINDOW_H
#define MAINWINDOW_H    //若MAINWINDOW_H 還沒被定義，就先定義它，避免重複包含

#include <QMainwindow>  //引入Qt主視窗

QT_BEGIN_NAMESPACE
namespace ui {class mainwindow; }
QT_END_NAMESPACE                                 //Qt空間命名，並宣告類別(由Qt designer自動生成)

class mainwindow : public QMainwindow {          //定義主視窗類別mainwindow，繼承自QMainwindow
    Q_OBJECT                                     //Qt的宏(處理器指令)

public :
    mainwindow (QWidget *parent = nullptr)       //建構子：初始化視窗
    ~mainwindow();                               //解構子：釋放資料

private slots:                                   //Qt專用的「槽函式」，用來接收事件
    void on_convertButton_clicked();             //當convert按鈕被點，執行函式

private:
    ui::mainwindow *ui ;                         //控制畫面上的元件

    Qstring dec_to_bin(int dec);
    Qstring dec_to_hex(int dec);
    int bin_to_dec(Qstring bin);
    int hex_to_dec(Qstring hex);
};

#endif                                           //結束，防重複包含