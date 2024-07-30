import discord
import random
from discord.ext import commands, tasks

# تعريف البوت وإعداداته
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# توكن البوت
TOKEN = ''

# قناة الديسكورد التي سيتم إرسال الصور إليها
CHANNEL_ID = 

# قائمة بروابط الصور العشوائية
random_car_images = [
    'https://pbs.twimg.com/media/EfsIwZ2XYAAmXZB?format=jpg&name=large',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Wikipedia_Final_v3.png/420px-Wikipedia_Final_v3.png',
    'https://cars.usnews.com/static/images/Auto/izmo/322686/2011_toyota_camry_angularfront.jpg',
    'https://static1.hotcarsimages.com/wordpress/wp-content/uploads/2021/03/A-Black-Infiniti-G35.jpg',
    'https://i.ytimg.com/vi/HN0CfWAH2bM/maxresdefault.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/BMW_M3_E36_purple.jpg/800px-BMW_M3_E36_purple.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Lexus_LS_400_UCF10_I.jpg/640px-Lexus_LS_400_UCF10_I.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/9/9d/2021_Ferrari_Roma_in_Rosso_Fiorano%2C_front_right.jpg',
    'https://www.bugatti.com/media/5lobscny/gallery6.png?cc=0,0.19006983515326048,0,0.06853040209466364&width=1920&height=900&rnd=133343651203970000',
    'https://di-uploads-pod46.dealerinspire.com/unioncitycdjrfiat/uploads/2023/05/2023DodgeChargerSRTHellcatwidebody-exterior-01.jpg',
    'https://www.slashgear.com/img/gallery/heres-what-makes-the-toyota-supra-mk4-one-of-the-coolest-jdm-cars-ever-built/intro-1706652078.jpg',
    'https://images.prismic.io/carwow/308bade4-bc03-4a29-a195-70631f39284a_2017+Nissan+GT-R+front+quarter+static.jpg',
    'https://www.cnet.com/a/img/resize/f6857e094a0cd0b546018159bf383679dd774942/hub/2018/10/05/549723f8-b454-4ab3-8c97-c31e422f707a/avalon-ogi.jpg?auto=webp&fit=crop&height=900&width=1200',
    'https://static.overfuel.com/dealers/trust-auto/image/1957-Chevy-Belair-Red-1024x683.jpg',
    'https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/15q2/657948/2016-cadillac-cts-v-test-review-car-and-driver-photo-660007-s-original.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/2011_Toyota_FJ_Cruiser_%28GSJ15R%29_wagon_%282011-11-08%29_01.jpg/800px-2011_Toyota_FJ_Cruiser_%28GSJ15R%29_wagon_%282011-11-08%29_01.jpg',
    'https://assets-global.website-files.com/62f50791f9b93f9c60c6b70a/6560c3487dee9697974d14de_Honda_Accord_(CV3)_EX_eHEV%2C_2021%2C_front.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/e/ea/Skoda_Octavia_IV_liftback_%28cropped%29.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuFEuko00WYi6kLHu8KCHO20BhQPATrBh3hg&s',
    'https://cdn.dealeraccelerate.com/raleigh/10/2032/51172/1920x1440/1964-chevrolet-impala-ss',
    'https://www.edmunds.com/assets/m/mitsubishi/lancer-evolution/2003/oem/2003_mitsubishi_lancer-evolution_sedan_base_fq_oem_1_500.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/a/a6/Mazda_Miata_-_002.jpg',
    'https://www.motortrend.com/uploads/sites/5/2020/09/2021-Mercedes-Benz-S-500-S-580-4Matic-59.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/2024-hyundai-elantra-limited-106-64ef85e2044f5.jpg?crop=0.661xw:0.496xh;0.197xw,0.381xh&resize=1200:*',
    'https://cdn.dealeraccelerate.com/motorcar/1/1148/29662/1920x1440/1987-toyota-land-cruiser-fj60',
    'https://di-uploads-pod3.dealerinspire.com/kiacountryofcharleston/uploads/2022/01/Stingersw2.png',
    'https://s3.eu-central-1.amazonaws.com/v3-ncg.motory.com/vehicle-new/1000x750/l-1635675009.9837-617e6b81f02b2.webp',
    'https://www.motortrend.com/uploads/2023/09/2024-Ford-F-150-Lariat-1.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7NRpmcd5x_U82Mit6K5jWkUuGnFEyYYszSg&s',
    'https://hips.hearstapps.com/hmg-prod/images/2024-chevrolet-camaro-ss-collectors-edition-1-647e1933c6c20.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/2023-audi-r8-gt-front-three-quarters-motion-3-1664827965.jpg?crop=0.595xw:0.668xh;0.0705xw,0.224xh&resize=768:*',
    'https://cdn.motor1.com/images/mgl/P3nO74/s3/2000-nissan-skyline-r34-gt-r-by-kaizo-industries-driven-by-paul-walker-in-fast-and-furious-bonham-s-auction.jpg',
    'https://imgd.aeplcdn.com/1920x1080/cw/ec/9725/Nissan-Sunny-Exterior-114974.jpg?wm=0&q=80&q=80',
    'https://static1.topspeedimages.com/wordpress/wp-content/uploads/2023/01/datsun-240z.jpg',
    'https://static.cargurus.com/images/forsale/2023/09/27/07/20/1981_buick_regal-pic-5922568396802779653-1024x768.jpeg',
    'https://www.dodge.com/content/dam/fca-brands/na/dodge/en_us/2023/challenger/vlp/desktop/MY23Challenger_VLP_Desktop_Exterior3.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/9/9b/Hyundai_Coup%C3%A9_J2.JPG',
    'https://www.cnet.com/a/img/resize/59094fc52b21ab3a70e339f46be85e9b13e8d7af/hub/2020/03/29/2ff119be-2d7d-49aa-89f4-dc4d7443fe9b/2021-genesis-g80-002.jpg?auto=webp&fit=crop&height=675&width=1200',
    'https://www.edmunds.com/assets/m/cs/blta7a14aa335ede638/6621fc52ca88743e8ded1504/2024_porsche_911-s-t_front.jpg',
    'https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_detail/concept/estoque/gallery/Lamborghini-Estoque-02_M.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Lamborghini_Countach_-_Flickr_-_exfordy_%282%29.jpg/1200px-Lamborghini_Countach_-_Flickr_-_exfordy_%282%29.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/b/bb/2023_Lamborghini_Aventador_Ultimae.jpg',
    'https://cdn.motor1.com/images/mgl/NROq2/s3/2020-aston-martin-db11.jpg',
    'https://media.ed.edmunds-media.com/gmc/yukon/2013/oem/2013_gmc_yukon_4dr-suv_denali_fq_oem_1_1600.jpg',
    'https://s1.almuraba.net/wp-content/uploads/2022/02/%D9%85%D8%A7%D8%B2%D8%AF%D8%A7-6-2022-1.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Subaru_Impreza_WRX_STI_-_Blue_%28cropped%29.jpg/1200px-Subaru_Impreza_WRX_STI_-_Blue_%28cropped%29.jpg',
    'https://static.wikia.nocookie.net/nfs/images/7/7f/NFSUB_Garage_Honda_CivicTypeR2000.jpg/revision/latest?cb=20230218183056&path-prefix=en',
    'https://hips.hearstapps.com/hmg-prod/images/2022-ford-mustang-shelby-gt500-02-1636734552.jpg?crop=0.845xw:1.00xh;0.0657xw,0&resize=768:*',
    'https://imageio.forbes.com/specials-images/imageserve/650ca116324527f1d6ef25c3/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds',
    'https://bringatrailer.com/wp-content/uploads/2022/01/1991_chevrolet_caprice_3h2a6026-1-48191.jpg',
    'https://hips.hearstapps.com/autoweek/assets/s3fs-public/130139995.jpg',
    'https://editorial.pxcrush.net/carsales/general/editorial/ge4719173455184780904.jpg?width=1024&height=682',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzSZ5xphQNkXNpscKyPEtuluCGFt0XDJnv5w&s',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Orange_Enzo_Ferrari_%287191948164%29.jpg/640px-Orange_Enzo_Ferrari_%287191948164%29.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/6/65/Porsche_Carrera_GT_-_Goodwood_Breakfast_Club_%28July_2008%29.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/2024-rolls-royce-phantom-102-64bad70ba7661.jpg?crop=0.498xw:0.446xh;0.300xw,0.332xh&resize=640:*',
    'https://i.gaw.to/content/photos/55/21/552190-land-rover-range-rover-2023-la-cinquieme-generation-du-premier-vus-de-luxe.jpeg',
    'https://hips.hearstapps.com/hmg-prod/images/2023-bentley-continental-gt-s-coupe-101-1654526518.jpg?crop=0.678xw:0.763xh;0.116xw,0.176xh&resize=768:*',
    'https://bringatrailer.com/wp-content/uploads/2023/01/1988_jaguar_xj-s-v12_img_0022-78030.jpeg?fit=940%2C626',
    'https://cdn.motor1.com/images/mgl/g4MN9E/s3/chevrolet-malibu.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Dodge_Viper_SRT-10.jpg/800px-Dodge_Viper_SRT-10.jpg',
    'https://www.assayyarat.com/wp-content/uploads/2023/08/1174444-640x360.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/2025-bmw-m5-139-667b0f49f2fca.jpg?crop=0.795xw:0.596xh;0.0881xw,0.334xh&resize=1200:*',
    'https://upload.wikimedia.org/wikipedia/commons/e/e6/Lada_2107_aka_Lada_Riva_October_1995_1452cc.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Hyundai_Kona_%28SX2%29_IMG_8762_%28cropped%29.jpg/1200px-Hyundai_Kona_%28SX2%29_IMG_8762_%28cropped%29.jpg',
    'https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/wp-content/uploads/2016/09/2017-Mercedes-AMG-GT-R-106.jpg?crop=0.877xw:0.719xh;0.0962xw,0.163xh&resize=1200:*',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Seat_850_Sport_Jarama_2006.JPG/1280px-Seat_850_Sport_Jarama_2006.JPG',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mitsubishi_V98_Pajero_Long_Body_Super_Exceed_3200_DI-D.JPG/800px-Mitsubishi_V98_Pajero_Long_Body_Super_Exceed_3200_DI-D.JPG',
    'https://cdn.dealeraccelerate.com/international/1/367/19729/1920x1440/1994-nissan-silvia',
    'https://media.ed.edmunds-media.com/dodge/charger/2010/oem/2010_dodge_charger_sedan_rt_fq_oem_2_1600.jpg',
    'https://carfax-vrs.imgix.net/2001-Toyota-Camry-EX-Marketing-04.jpg',
    'https://ymimg1.b8cdn.com/uploads/car_model/7297/pictures/7434236/2019_Toyota_Rush__1_.png',
    'https://upload.wikimedia.org/wikipedia/commons/1/13/2019_Suzuki_Jimny_SZ5_4X4_Automatic_1.5.jpg',
    'https://nissanautoegypt.com/wp-content/uploads/2019/09/d.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/chevrolet-corvette-2001-306568-1509730166.jpg?crop=0.6666666666666666xw:1xh;center,top&resize=1200:*',
    'https://65e81151f52e248c552b-fe74cd567ea2f1228f846834bd67571e.ssl.cf1.rackcdn.com/Ferrari/Model%20Pages/488%20Spider/ferrari-488-spider-red-driving.jpg',
    'https://cdn.pixabay.com/photo/2016/11/30/15/34/car-1873116_1280.jpg',
    'https://cdn3.focus.bg/autodata/i/renault/logan/logan/large/1a4e8c8dad8a3ccd49ac62318ce3e17f.jpg',
    'https://www.topgear.com/sites/default/files/cars-car/image/2023/04/5_90.jpg',
    'https://www.thepaddockmagazine.com/wp-content/uploads/2023/04/00001-1.jpeg',
    'https://www.microlise.com/wp-content/uploads/2020/11/P_TGX_EOT_Showtruck-01-1920x960-1.jpg',
    'https://www.motorindiaonline.in/wp-content/uploads/2022/09/Mercedes-Benz-Trucks-pic-1.jpg',
    'https://marvel-b1-cdn.bc0a.com/f00000000269980/s18391.pcdn.co/wp-content/uploads/2024/02/volvotruck2-14001-1000x500.jpg',
    'https://static.wikia.nocookie.net/ford/images/d/d5/950.jpg/revision/latest?cb=20220519192939',
    'https://bringatrailer.com/wp-content/uploads/2023/05/1997_alfa-romeo_155_1m6a8893-edit-06761.jpg',
    'https://static1.hotcarsimages.com/wordpress/wp-content/uploads/2020/08/carmagazinecouk-Lotus-Elise.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4hdUK-ujsMnq1-jL0UFlpitYdtiZPuohD_A&s',
    'https://cdn.motor1.com/images/mgl/y2PgRq/s1/2024-porsche-cayenne.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Lamborghini_Urus_19.09.20_JM_%282%29_%28cropped%29.jpg/1200px-Lamborghini_Urus_19.09.20_JM_%282%29_%28cropped%29.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQujttaOcT4JAVbY6NaqGpa0ZGjGU7djmUY7A&s',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Pagani_Zonda_C12_%27chassis_001%27_Genf_2019_1Y7A5539.jpg/1200px-Pagani_Zonda_C12_%27chassis_001%27_Genf_2019_1Y7A5539.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Toyota_GR_Yaris_%28XP21%29_%E2%80%93_f_03052021.jpg/640px-Toyota_GR_Yaris_%28XP21%29_%E2%80%93_f_03052021.jpg',
    'https://www.motortrend.com/uploads/2023/07/2024-cadillac-xt4-deep-dive-1.jpg?w=768&width=768&q=75&format=webp',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJ5kuxIoPaDMmYNBifaxEy-0EtytvtmD_IQg&s',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Nissan_Qashqai_Mk2_Facelift.jpg/1200px-Nissan_Qashqai_Mk2_Facelift.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/cd12dn92e-1604609584.jpg?crop=0.708xw:0.932xh;0.155xw,0&resize=1200:*',
    'https://cdn.motor1.com/images/mgl/KLnrM/s1/abarth-f595.jpg',
    'https://www.sportscarmarket.com/profile/1970-mazda-cosmo-110s/attachment/1970-mazda-cosmo-110s-front', 
    'https://upload.wikimedia.org/wikipedia/commons/0/0b/1968_AMC_AMX_390_Go_Package%2C_front_left_%28Cruisin%27_the_River_Lowellville_Car_Show%2C_June_19th%2C_2023%29.jpg',
    'https://hips.hearstapps.com/hmg-prod/images/2024-subaru-brz-ts-125-658066d817df4.jpg?crop=0.556xw:0.625xh;0.288xw,0.245xh&resize=768:*',
    'https://www.carscoops.com/wp-content/uploads/2015/11/2016-Fiat-Tipo-130.jpg',

    # قم بإضافة المزيد من روابط الصور هنا
]

# مهمة مجدولة لإرسال صورة السيارة كل ساعة
@tasks.loop(hours=12)
async def send_hourly_car_image():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        image_url = random.choice(random_car_images)
        await channel.send(image_url)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # بدء المهمة المجدولة بعد أن يكون البوت جاهزًا
    send_hourly_car_image.start()

# تشغيل البوت
bot.run(TOKEN)
