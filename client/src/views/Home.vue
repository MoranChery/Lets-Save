<template>
  <div class="home">
    <div class="filter">
      <img class="logo-img" src="../assets/logo.png" alt="Logo">
      <b-card title="ברוכים הבאים ל-Smart Save" style="max-width: 80rem;" class="mb-lg-0" img-alt="Image" img-top>
        <b-card-text>אתר זה נוצר בכדי לאפשר השוואה בין מגוון קופות גמל להשקעה בישראל.</b-card-text>
        <b-card-text>ראיתי צורך לבנות אתר זה כדי לאפשר לאנשים להשואות קופות גמל באמצעות מחשבון פשוט והמלצות המערכת המבוססות על נתונים לפי בקשת המשתמש.</b-card-text>
        <b-card-text>תמיד חשבתי כיצד לחסוך את כספי בצורה חכמה ויעילה. הפחד שלי היה שבגלל חוסר ידע הייתי מאבד את הכסף שרציתי להשקיע בצורה חכמה.</b-card-text>
        <b-card-text>לאחר חיפוש ארוך מצאתי מידע על קופות גמל להשקעה, אך גם כשמצאתי את המידע ורציתי לבחון ולהשואות הצעות שונות היה קשה לעשות זאת.</b-card-text>
        <b-card-text>אציין, אני מהנדסת מערכות מידע, ברגע שהבנתי שיש לי את הכוח והיכולת להביא לשינוי החלטתי לעשות זאת.</b-card-text>
      </b-card>
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
    direction: rtl;
    height: 100%;
    text-align: justify;
    font-size: 18px;
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
  .card {
    margin: 0 auto; /* Added */
    float: none; /* Added */
    margin-bottom: 10px; /* Added */
}
</style>
