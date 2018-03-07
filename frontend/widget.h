#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGraphicsScene>

#include <triangle.h>
#include <circle.h>

#include <vector>

#include <QNetworkRequest>
#include <QNetworkReply>

using std::vector;
namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();
public slots:
    void updateCoordinates();
    void receiveCoordinates(QNetworkReply*);

private:
    Ui::Widget        *ui;
    QGraphicsScene    *scene;     // Объявляем графическую сцену
    vector<Triangle*> ble;  // и треугольник
    vector<Circle*>   obj;
    QNetworkAccessManager *manager;
    QNetworkRequest   createRequest();
    void              sendRequest();
//    void repaint();
};

#endif // WIDGET_H
