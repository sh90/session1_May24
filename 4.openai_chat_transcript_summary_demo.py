from openai import OpenAI
import data_info
client = OpenAI(api_key=data_info.open_ai_key)

transcript = """
Customer:
Hi, I ordered a blender from your website last week, and when it arrived, it was damaged. The box was dented, and the blender has a crack on the base. I’d like to know what I can do to get a replacement or refund.

Customer Support:
Hello, and thank you for reaching out to us. I’m really sorry to hear that your blender arrived damaged. I completely understand how disappointing that must be. I’ll be happy to assist you in getting this sorted. Could you please provide me with your order number so I can look into it?

Customer:
Sure! My order number is 123456789.

Customer Support:
Thank you for providing your order number. I’ll take a look at the details right away. One moment, please.

[A few seconds pass]

Customer Support:
I’ve located your order. I can see that you ordered a “TurboBlender X1000.” I’m really sorry for the inconvenience you’ve experienced with the damaged item. To move forward, I’ll need a bit more information. Could you please send me a photo of the damaged blender, including the crack on the base and the condition of the packaging?

Customer:
Sure! Here’s a photo of the blender and the damaged packaging.

[Customer uploads photo]

Customer Support:
Thank you for the photo. I can see the crack on the base and the damage to the packaging. It looks like the item was unfortunately damaged during shipping. Again, I apologize for this experience.

We can offer you two options to resolve this:

A replacement unit sent to you at no additional charge, or

A full refund for your purchase.

Which option would you prefer?

Customer:
I’d like a replacement, please. I really need the blender and was excited to use it, but I can’t with it being cracked like this.

Customer Support:
Thank you for your patience, and I’m glad to hear you’d like a replacement! I’ll arrange for a new blender to be shipped out to you immediately. The shipping process may take 3-5 business days depending on your location. You’ll also receive a prepaid return label so you can send the damaged blender back to us at no extra cost.

I’ll take care of everything for you now. Is there anything else I can assist you with while we handle this?

Customer:
That sounds good. Can you also confirm whether the replacement will arrive in better packaging this time? I’m concerned that it might get damaged again in transit.

Customer Support:
Absolutely! I understand your concern, and I’ve made a note of that in your order. Our warehouse team will ensure the replacement is securely packaged, and we’ll also add extra protection to prevent any damage during shipping.

You should be all set, and we’ll also send you a tracking number for your new shipment as soon as it’s on its way.

Customer:
Perfect! I really appreciate your help with this.

Customer Support:
You’re very welcome! We truly value your business, and I’m happy we could resolve this for you. Is there anything else I can assist you with today? Maybe a question about your new blender or anything else?

Customer:
Actually, I have one more question. Do you offer any warranty on the blender? I’d like to make sure it’s covered in case there are any issues down the line.

Customer Support:
Great question! Yes, all of our blenders come with a 1-year warranty that covers any manufacturing defects. If anything goes wrong with your new blender within the first year, just reach out to us, and we’ll be happy to assist with repairs or a replacement.

Customer:
That’s good to know, thank you. I didn’t realize it had a warranty!

Customer Support:
You're welcome! I'm happy to provide that info. Having the warranty definitely adds peace of mind, especially for kitchen appliances like blenders that get a lot of use. If you have any other questions about the warranty or anything else, just let me know.

Customer:
Will I get an email confirming the replacement? Just to have everything in writing.

Customer Support:
Yes, absolutely. You’ll receive an email shortly confirming the replacement and tracking information. The email will include all the details about the replacement process, including the return label for the damaged item.

Customer:
Great, I’ll look out for that. Thanks again for everything!

Customer Support:
You’re very welcome! If you need anything else, don’t hesitate to reach out. I hope you enjoy your new blender once it arrives! Have a wonderful day.

Customer:
You too! Thanks for your help. 😊

Customer Support:
It’s been a pleasure assisting you. Take care!

"""
response = client.responses.create(
    model="gpt-4o-mini",
    input= "Can you summarize given chat transcript in under 150 words\n" + transcript
)

print(response.output_text)
