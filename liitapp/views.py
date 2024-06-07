from django.shortcuts import render, redirect, get_object_or_404
from .models import Register
import uuid
import qrcode
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from io import BytesIO
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        leaderName = request.POST.get('leaderName')
        member1 = request.POST.get('member1')
        member2 = request.POST.get('member2')
        member3 = request.POST.get('member3')
        email = request.POST.get('email')
        mobileNumber = request.POST.get('mobileNumber')
        domain = request.POST.get('domain')
        designation1 = request.POST.get('designation1')
        designation2 = request.POST.get('designation2')
        designation3 = request.POST.get('designation3')
        designation4 = request.POST.get('designation4')
        college = request.POST.get('college')
        
        uploaded_file = request.FILES.get('uploaded_file')  # Get the uploaded file
        
        unique_id = uuid.uuid4().hex[:6]
        
        # Create a new Register object and save it
        register = Register(
            leaderName=leaderName,
            member1=member1,
            member2=member2,
            member3=member3,
            email=email,
            mobileNumber=mobileNumber,
            domain=domain,
            designation1=designation1,
            designation2=designation2,
            designation3=designation3,
            designation4=designation4,
            college=college,
            unique_id=unique_id,
            uploaded_file=uploaded_file  # Assign the uploaded file to the model field
        )
        register.save()

        return redirect('completeRegister', register_id=register.pk)
    else:
        return render(request, 'index.html')

def completeRegister(request, register_id):
    register = get_object_or_404(Register, id=register_id)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    qr.add_data(f"Registration ID: {register.unique_id}")
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Convert the QR code image to BytesIO for attaching to the email
    qr_img_io = BytesIO()
    qr_img.save(qr_img_io, format='PNG')
    qr_img_io.seek(0)

    # Create and email
    subject = 'Registration Confirmation'
    to_email = [register.email]  # Replace with the actual field name storing the customer's email

    # Render email template
    html_message = render_to_string('registration_confirmation_email.html', {'register': register})
    plain_message = strip_tags(html_message)

    # Create email
    email = EmailMessage(subject, plain_message, to=to_email)

    # Attach QR code to email
    email.attach('registration.png', qr_img_io.read(), 'image/png')

    # Send email
    #email.send()

    return render(request, 'completeRegister.html')

def viewRegistrations(request):
    register = Register.objects.all()
    return render(request, 'viewRegistrations.html', {'register': register})