//#ifndef WIDGET_H
//#define WIDGET_H

//#include <QWidget>

//namespace Ui {
//class Widget;
//}

//class Widget : public QWidget
//{
//    Q_OBJECT

//public:
//    explicit Widget(QWidget *parent = 0);
//    ~Widget();

//private:
//    Ui::Widget *ui;
//};

//#endif // WIDGET_H


#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGraphicsScene>

#include <triangle.h>
#include <circle.h>

#include <vector>

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

private:
    Ui::Widget        *ui;
    QGraphicsScene    *scene;     // Объявляем графическую сцену
    vector<Triangle*> ble;  // и треугольник
    vector<Circle*>   obj;
//    void repaint();
};

#endif // WIDGET_H
