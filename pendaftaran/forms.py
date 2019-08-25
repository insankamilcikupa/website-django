from django import forms
# from.models import DaftarSiswa

# class DaftarForm(forms.ModelForm):
#     class Meta:
#         model = DaftarSiswa
#         fields = [
#             'Nama_Lengkap',
#             'Tempat_Lahir',
#             'Tanggal_Lahir',
#             'Jenis_Kelamin',
#             'Alamat',
#             'Agama',
#             'Nama_Orang_Tua',
#             'Alamat_Orang_Tua',
#             'No_Telp_Orang_Tua',
#         ]
#         tahun = range(2000,2017,1)

#         labels = {
#             'Nama_Lengkap' : 'Nama Lengkap',
#             'Tempat_Lahir' : 'Tempat Lahir',
#             'Tanggal_Lahir' : 'Tanggal Lahir',
#             'Jenis_Kelamin' : 'Jenis Kelamin',
#             'Alamat' : 'Alamat',
#             'Agama' : 'Agama',
#             'Nama_Orang_Tua' : 'Nama Orang Tua',
#             'Alamat_Orang_Tua' : 'Alamat Orang Tua',
#             'No_Telp_Orang_Tua' : 'No.Telp Orang Tua',
#         }

#         widgets = {
#             'Nama_Lengkap': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Isi Nama Lengkap',
#                 }
#             ),

           
#             'Tanggal_Lahir': forms.SelectDateWidget(
#                 years = tahun,
#                 attrs = {
#                     'class':'form-control col-row-sm-1',
#                 }
#             ),

#             'Tempat_Lahir': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Isi Tempat Lahir',
#                 }
#             ),

#             'Jenis_Kelamin': forms.Select(
#                 attrs = {
#                     'class':'form-control col-sm-2',
#                 }
#             ),

#             'Alamat': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Isi Alamat',
#                 }
#             ),

#             'Agama': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Isi Agama',
#                 }
#             ),

#             'Nama_Orang_Tua': forms.TextInput(
#                 attrs = {
#                     'class':'form-control',
#                     'placeholder':'Isi Nama Orang Tua',
#                 }
#             ),

        #     'Alamat_Orang_Tua': forms.TextInput(
        #         attrs = {
        #             'class':'form-control',
        #             'placeholder':'Alamat Orang Tua',
        #         }
        #     ),

        #     'No_Telp_Orang_Tua': forms.TextInput(
        #         attrs = {
        #             'class':'form-control',
        #             'placeholder':'Isi No. Telp yang dapat dihubungi',
        #         }
        #     ),
        # }
