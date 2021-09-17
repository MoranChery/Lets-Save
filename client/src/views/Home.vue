<template>
  <div class="home">
    <div class="filter">
    <img class="logo-img" src="../assets/logo.png" alt="Logo">
    <div class="css-typing">
      <h2>ברוכים הבאים ל-Smart Save</h2>
      <p>אתר זה נוצר בכדי לאפשר השוואה בין מגוון קופות גמל להשקעה בישראל.</p>
      <p>ראיתי צורך לבנות אתר זה כדי לאפשר לאנשים להשואות קופות גמל באמצעות מחשבון פשוט והמלצות המערכת המבוססות על נתונים לפי בקשת המשתמש.</p>
       <p>תמיד חשבתי כיצד לחסוך את כספי בצורה חכמה ויעילה. הפחד שלי היה שבגלל חוסר ידע הייתי מאבד את הכסף שרציתי להשקיע בצורה חכמה.</p>
       <p>לאחר חיפוש ארוך מצאתי מידע על קופות גמל להשקעה, אך גם כשמצאתי את המידע ורציתי לבחון ולהשואות הצעות שונות היה קשה לעשות זאת.</p>
       <p>אציין, אני מהנדסת מערכות מידע, ברגע שהבנתי שיש לי את הכוח והיכולת להביא לשינוי החלטתי לעשות זאת.</p>
    </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
<style scoped>
  .filter{
    margin-top: 5%;
    margin-left: auto;
    margin-right: auto;
    width: 90%;
    direction: rtl;
    padding: 3%;
    background: rgb(106, 179, 179);
    height: 100%;
    text-align: justify;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 50px 0 rgba(0, 0, 0, 0.19);
  }
  .logo-img{
    border-radius: 300px;
    width: 200px;
    height: 200px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
  }
  .css-typing h2{
    direction: rtl;
    font-size: 25px;
    color: black;
    font-weight: bold;
  }
  .css-typing p {
    direction: rtl;
    font-size: 18px;
    color: #090952;
    font-weight: bold;
  }
</style>
