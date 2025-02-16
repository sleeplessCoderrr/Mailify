<script lang="ts">
    import logoDark from '../assets/mailify-dark.png'
    import logoLight from '../assets/mailify-light.png'
    import {navigate} from "svelte-routing";

    function goToMailing(){navigate("/page/mailing");}
    function goToHome(){navigate("/");}
</script>

<header class="flex flex-row gap-48 justify-evenly items-center h-36 mx-auto font-helvetica">
    <div class="flex flex-row items-center gap-4">
        <img src={logoLight} class="w-14" alt="logo"/>
        <button on:click={goToHome} class="font-bold text-3xl">Mailify</button>
    </div>

    <div class="items-center bg-mist/20 py-2 px-12 rounded-md backdrop-blur-sm shadow-md border-2 border-stone-300">
        <ul class="flex gap-8">
            <a href="#" class="no-underline">Features</a>
            <a href="#" class="no-underline">Privacy Policy</a>
            <a href="#" class="no-underline">FAQ</a>
            <a href="#" class="no-underline">Contact Us</a>
        </ul>
    </div>

    <div class="items-center">
        <button class="font-medium text-midnight font-helvetica
                  border-solid border-2 border-midnight
                  rounded-md py-2 px-4
                  bg-blaze/80 backdrop-blur shadow-md
                  hover:bg-blaze ease-in-out duration-300"
                  on:click={goToMailing()}>Get Started Free</button>
    </div>
</header>