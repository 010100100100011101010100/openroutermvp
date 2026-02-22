from models.billing import Billing
from models.user import User
from dodopayments import DodoPayments
import os
from datetime import datetime

client=DodoPayments(
    bearer_token=os.environ.get("DODO_PAYMENTS_BEARER_TOKEN"),
    environment="test_mode"
)

async def create_payment(uid:str,amount:float,currency:str="USD")->str:
        user=User.objects(uid=uid).first()
        credits=int(amount)*100
        checkout_session=client.checkout_sessions.create(
                product_cart=[{"product_id":"ai_credits","quantity":credits}],
                customer={"email":user.email},
                return_url="http://localhost:3000/checkout/success"
        )   
        return checkout_session.url


async def handle_webhook(event):
        if event.type=="payment.succeeded":
            uid=event.metadata["uid"]
            credits=int(event.metadata["credits"])
            amount=float(event.metadata["amount"])
            user=User.objects(uid=uid).first()
            user.creditbalance+=credits
            user.save()
            billing_record=Billing(user=user,amount=amount,billing_date=datetime.now(),credits_added=credits)
            billing_record.save()
        elif event.type=="payment.failed":
            return {"status":"payment_failed"}
        else:
            return {"status":"Payment event_not_handled by Dodo"}
        