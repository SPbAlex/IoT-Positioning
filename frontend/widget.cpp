#include "widget.h"
#include "ui_widget.h"

#include <QTimer>
#include <qdebug.h>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    this->resize(600,600);          // Задаем размеры виджета, то есть окна
    this->setFixedSize(600,600);    // Фиксируем размеры виджета

    scene = new QGraphicsScene();   // Инициализируем графическую сцену
//    ble = new Triangle[4];      // Инициализируем треугольник
//    obj = new Circle[2];

    for(int i = 0; i < 4; i++)
        ble.push_back(new Triangle());
    for(int i = 0; i < 2; i++)
        obj.push_back(new Circle());
    ui->graphicsView->setScene(scene);  // Устанавливаем графическую сцену в graphicsView
    ui->graphicsView->setRenderHint(QPainter::Antialiasing);    // Устанавливаем сглаживание
    ui->graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff); // Отключаем скроллбар по вертикали
    ui->graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff); // Отключаем скроллбар по горизонтали
    ui->graphicsView->resize(600,600);
    scene->setSceneRect(-300,-300,300,300); // Устанавливаем область графической сцены

//    scene->addLine(-300,0,300,0,QPen(Qt::black));   // Добавляем горизонтальную линию через центр
//    scene->addLine(0,-300,0,300,QPen(Qt::black));   // Добавляем вертикальную линию через центр

    for(int i = 0; i < 4; i++)
        scene->addItem(ble[i]);   // Добавляем на сцену треугольник
    for(int i = 0; i < 2; i++)
        scene->addItem(obj[i]);

    obj[0]->setPos(-200,-100);
    obj[1]->setPos(-50,-70);

    ble[0]->setPos(-400,-400);
    ble[1]->setPos(100,-400);
    ble[2]->setPos(-400,100);
    ble[3]->setPos(100,100);

    ble[0]->setRotation(135);
    ble[1]->setRotation(225);
    ble[2]->setRotation(45);
    ble[3]->setRotation(315);

    QTimer *timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(updateCoordinates()));
    timer->start(1000);
//    manager = new QNetworkAccessManager(this);
//    connect(manager, SIGNAL(finished(QNetworkReply*)),
//            this, SLOT(replyFinished(QNetworkReply*)));
}

void Widget::updateCoordinates() {
//    manager->get(QNetworkRequest(QUrl("http://localhost:8000/get_coords")));
    //    obj[0]->setPos(-10,-200);
    //    obj[1]->setPos(-170,-50);
    //    scene->update();
}
Widget::~Widget()
{
    delete ui;
}
