<script lang="ts">
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import HomeBackground from "../components/background/HomeBackground.svelte";
</script>

<div class="flex-col justify-items-center items-center w-full">
    <HomeBackground/>
    <main class="flex-column w-full items-center justify-items-center">
        <Navbar/>

        <div class="flex-column justify-items-center">
            <div class="flex flex-row gap-4 self-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 self-center bg-blaze rounded p-0 stroke-stone-200">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                </svg>
                <p class="text-base my-4 font-medium">KNOW EVERY PARAMETER IN EASY REACH</p>
            </div>
            <p class="text-8xl  my-6 font-semibold">Control Your Car</p>
            <p class="text-8xl  my-6 font-medium">Via Your Phone</p>
        </div>

        <Footer/>
    </main>
</div>