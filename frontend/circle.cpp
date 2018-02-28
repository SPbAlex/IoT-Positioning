#include "circle.h"


Circle::Circle() :
    QGraphicsItem()
{

}

Circle::~Circle()
{

}

QRectF Circle::boundingRect() const
{
    return QRectF(-15,-15,15,15);   // Ограничиваем область, в которой лежит треугольник
}

void Circle::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
        QPolygon polygon;   // Используем класс полигона, чтобы отрисовать круг
        // Помещаем координаты точек в полигональную модель
        polygon << QPoint(-15,-15) << QPoint(-15,15) << QPoint(15,15) << QPoint(15,-15);
        painter->setBrush(Qt::red);     // Устанавливаем кисть, которой будем отрисовывать объект
        painter->drawPolygon(polygon);  // Рисуем треугольник по полигональной модели
        Q_UNUSED(option);
        Q_UNUSED(widget);
}
