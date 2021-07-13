from datetime import datetime

from asgiref.sync import sync_to_async
from django.core.mail import EmailMessage

from prueba_omni import settings

NOTIFICATION_SEND_MAIL_SUBJECT = "Notificaion del envio de Orden {orden}"
NOTIFICATION_SEND_MAIL_MESSAGE = "Se informa que  la Orden {orden}  con los productos {productos} fue enviado el dia " \
                                 "{fecha} "

NOTIFICATION_DELIVERY_MAIL_SUBJECT = "Notificaion del recepcion de la Orden {orden}"
NOTIFICATION_DELIVERY_MAIL_MESSAGE = "Se informa que se ha recibido el paquete  de la Orden {orden}  con los " \
                                     "productos {productos} el dia {fecha} "


async def send_email_send_shipmet(shipment):
    try:

        list_products = [product.name for product in shipment.products.all()]

        subject = NOTIFICATION_SEND_MAIL_SUBJECT.format(orden=str(shipment.order))
        message = NOTIFICATION_SEND_MAIL_MESSAGE.format(orden=str(shipment.order), productos="\n -".join(list_products),
                                                        fecha=shipment.send_date)
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[shipment.order.user.email]
        )

        email.send()
        response = {"status": "OK", "message": "Mensaje enviado"}
    except Exception as e:
        response = {"status": "FAIL", "message": "Mensaje enviado"}

    return response

@sync_to_async()
def send_email_delivery_shipmet(shipment):
    try:

        list_products = [product.name for product in shipment.products.all()]

        header = NOTIFICATION_DELIVERY_MAIL_SUBJECT.format(orden=str(shipment.order))
        message = NOTIFICATION_DELIVERY_MAIL_MESSAGE.format(orden=str(shipment.order),
                                                            productos="\n -".join(list_products),
                                                            fecha=shipment.delivery_date)
        email = EmailMessage(
            header,
            message,
            settings.EMAIL_HOST_USER,
            [shipment.order.user.email]
        )

        email.send()
        response = {"status": "OK", "message": "Mensaje enviado"}
    except Exception as e:
        response = {"status": "FAIL", "message": "Mensaje enviado"}

    return response
