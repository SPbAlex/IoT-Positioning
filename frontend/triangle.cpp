#include "triangle.h"

Triangle::Triangle() :
    QGraphicsItem()
{

}

Triangle::~Triangle()
{

}

QRectF Triangle::boundingRect() const
{
    return QRectF(-15,-20,20,30);   // Ограничиваем область, в которой лежит треугольник
}

void Triangle::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
        QPolygon polygon;   // Используем класс полигона, чтобы отрисовать треугольник
        // Помещаем координаты точек в полигональную модель
        polygon << QPoint(0,-20) << QPoint(15,20) << QPoint(-15,20);
        painter->setBrush(Qt::blue);     // Устанавливаем кисть, которой будем отрисовывать объект
        painter->drawPolygon(polygon);  // Рисуем треугольник по полигональной модели
        Q_UNUSED(option);
        Q_UNUSED(widget);
}
