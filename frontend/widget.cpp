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
    timer->start(2000);
    manager = new QNetworkAccessManager(this);
//    connect(manager, SIGNAL(finished(QNetworkReply*)),
//            this, SLOT(receiveCoordinates(QNetworkReply*)));
    QObject::connect(manager, &QNetworkAccessManager::finished,
            this, [=](QNetworkReply *reply) {
                if (reply->error()) {
                    qDebug() << reply->errorString();
                    return;
                }
                QString answer = reply->readAll();
                QRegExp rx("(\d*\.\d*)");
//                qDebug() << answer;
                QStringList list;
                int pos = 0;

                while ((pos = rx.indexIn(answer, pos)) != -1) {
                    list << rx.cap(1);
                    pos += rx.matchedLength();
                }
                qDebug() << list;
            }
        );
}

void Widget::updateCoordinates() {
    sendRequest();
    //    obj[0]->setPos(-10,-200);
    //    obj[1]->setPos(-170,-50);
    //    scene->update();
}


QNetworkRequest Widget::createRequest() {
    QNetworkRequest request;
    request.setUrl(QUrl("http://10.30.36.28:8000/get_coords/"));
    request.setRawHeader("Content-Type","text/plain");
    // здесь прописываются все необходимые заголовки запроса
    return request;
}

void Widget::receiveCoordinates(QNetworkReply *reply) {
    QByteArray data=reply->readAll();
    qDebug() << data;
}
void Widget::sendRequest() {

    QNetworkRequest request = createRequest();
    manager->get(request);
}

Widget::~Widget()
{
    delete ui;
}
