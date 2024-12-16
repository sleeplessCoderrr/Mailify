<script lang="ts">
    import MailLogo from "./icon/MailIcon.svelte";
    import RightArrowIcon from "./icon/RightArrowIcon.svelte";
</script>

<div class="flex flex-col z-1 w-5/12 justify-items-center gap-4">
    <div class="flex flex-row bg-mist border-2 border-stone-300 rounded-md p-2 w-full justify-items-center">
        <div class="flex flex-row gap-2 w-full">
            <MailLogo props="size-6 self-center stroke-white"/>
            <input
                type="email"
                id="email"
                placeholder="Email Address"
                class="w-11/12 bg-transparent outline-none text-midnight"
            >
        </div>
        <button class="">
            <RightArrowIcon props="size-6 bg-blaze rounded stroke-white"/>
        </button>
    </div>
    <div>
        <p class="text-midnight">We'll never spam you. <a href="#" class="no-underline hover:underline">See our privacy policy</a> </p>
    </div>
</div>
