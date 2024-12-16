<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";
    import MailLogo from "../components/essentials/icon/MailIcon.svelte";
    import Write from "../components/essentials/Write.svelte";
    import TypeWriter from "../components/essentials/TypeWriter.svelte";
    import EmailLetter from "../components/essentials/EmailLetter.svelte";
</script>

<div class="flex-col justify-items-center items-center w-full font-helvetica">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center">
        <Navbar/>

        <div class="flex-column justify-items-center mt-2">
            <div class="flex flex-row gap-4 self-center">
                <MailLogo props="size-6 self-center bg-blaze rounded p-0 stroke-stone-200"/>
                <p class="text-base my-4 font-medium">
                    <TypeWriter
                        texts={
                        [
                          "TRANSFORM YOUR EMAILS, UNLOCK OPPORTUNITIES",
                          "TRANSFORM YOUR EMAILS, SEIZE NEW POSSIBILITIES",
                          "TRANSFORM YOUR EMAILS, OPEN DOORS TO SUCCESS",
                          "TRANSFORM YOUR EMAILS, CAPTURE THE ATTENTION YOU DESERVE"
                        ]}
                        speed={80}
                        loop={true}
                    />
                </p>
            </div>
            <p class="text-8xl my-6 font-medium text-center">
                <Write/> Email <br/> That Get Noticed
            </p>
        </div>

        <div class="w-full justify-items-center mt-96">
            <EmailLetter/>
        </div>

        <Footer/>
    </main>
</div>