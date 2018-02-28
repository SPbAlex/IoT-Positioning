#ifndef CIRCLE_H
#define CIRCLE_H

#include <QGraphicsItem>
#include <QPainter>

// Наследуемся от QGraphicsItem
class Circle : public QGraphicsItem
{
public:
    Circle();
    ~Circle();

protected:
    QRectF boundingRect() const;    /* Определяем виртуальный метод,
                                     * который возвращает область, в которой
                                     * находится треугольник
                                     * */
    /* Определяем метод для отрисовки треугольника
     * */
    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget);
};

#endif // CIRCLE_H
