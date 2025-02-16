<script lang="ts">
    export let isLoading: boolean = false; 
    export let progress: number = 0; 
    export let funFact: string = "Loading, please wait...";
    export let detail: string = ""; 
</script>

{#if isLoading}
<div class="fixed inset-0 flex flex-col items-center justify-center bg-white/90 z-50 gap-2 text-center">
    <div class="w-1/3 bg-mist rounded-md h-6 mt-4 relative">
        <span class="absolute inset-0 flex items-center justify-center text-white z-10">
            Generating Email...
        </span>
        <div
            class="bg-blaze h-6 rounded-md transition-all"
            style="width: {progress}%"
        ></div>
    </div>

    <div class="mt-48 absolute animate-bounce">
        <p class="text-lg font-semibold text-midnight">
            {funFact}
        </p>
        <p class="mt-1 text-sm text-midnight">
            {detail}
        </p>
    </div>
</div>
{/if}
