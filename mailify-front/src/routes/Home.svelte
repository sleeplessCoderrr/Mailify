<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";
    import MailLogo from "../components/essentials/icon/MailLogo.svelte";
    import Write from "../components/essentials/Write.svelte";
</script>

<div class="flex-col justify-items-center items-center w-full">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center">
        <Navbar/>

        <div class="flex-column justify-items-center">
            <div class="flex flex-row gap-4 self-center">
                <MailLogo/>
                <p class="text-base my-4 font-medium">TRANSFORM YOUR EMAILS, UNLOCK OPPORTUNITIES</p>
            </div>
            <p class="text-8xl my-6 font-semibold text-center">
                <Write/> Email <br/> That Get Noticed
            </p>
        </div>

        <Footer/>
    </main>
</div>