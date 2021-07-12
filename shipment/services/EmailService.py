from datetime import datetime

from django.core.mail import EmailMessage


from prueba_omni import settings

NOTIFICATION_SEND_MAIL_SUBJECT = "Notificaion del envio de {orden}"
NOTIFICATION_SEND_MAIL_MESSAGE = "Se informa que  la {orden}  con los productos {productos} fue enviado el dia {fecha} "

NOTIFICATION_DELIVERY_MAIL_SUBJECT = "Notificaion del recepcion de {orden}"
NOTIFICATION_DELIVERY_MAIL_MESSAGE = "Se informa que se ha recibido el paquete  de la {orden}  con los productos {" \
                                     "productos} el dia {fecha} "


async def send_email_send_shipmet(shipment):
    try :

        products = shipment.products.all();
        list_products = [product.name for product in products]

        subject = NOTIFICATION_SEND_MAIL_SUBJECT.format(orden=str(shipment.order))
        message = NOTIFICATION_SEND_MAIL_MESSAGE.format(orden=str(shipment.order), productos="\n -".join(list_products) ,
                                                        fecha=shipment.send_date)
        email = EmailMessage(
            subject= subject,
            body = message,
            from_email=settings.EMAIL_HOST_USER,
            to=[shipment.order.user.email]
        )
        # email.attach_file(ConsultSerializer.file)
        email.send()
        response = {"Mensaje enviado"}
    except Exception as e :
        response = {"Error enviando correo"}

    return response


async def send_email_delivery_shipmet(shipment):
    try :

        products = shipment.products.all();
        list_products = [product.name for product in products]

        header = NOTIFICATION_DELIVERY_MAIL_SUBJECT.format(orden=str(shipment.order))
        message = NOTIFICATION_DELIVERY_MAIL_MESSAGE.format(order=str(shipment.order),
                                                            productos="\n -".join(list_products) ,
                                                            dia=shipment.delivery_date)
        email = EmailMessage(
            header,
            message,
            settings.EMAIL_HOST_USER,
            [shipment.order.user.email]
        )

        email.send()
        response = {"Mensaje enviado"}
    except Exception as e :
        response = {"Error enviando correo"}

    return response


